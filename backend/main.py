from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from geoalchemy2.shape import to_shape
from geoalchemy2.functions import ST_AsGeoJSON
from geojson import Feature, FeatureCollection, Point as GeoPoint
import json

from database import get_db, engine, Base
from models import PointOfInterest, Region
from schemas import POICreate, POIResponse, RegionCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GIS Data Platform", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- POI endpoints ----------

@app.get("/api/pois", response_model=list[POIResponse])
def list_pois(db: Session = Depends(get_db)):
    return db.query(PointOfInterest).all()


@app.get("/api/pois/geojson")
def list_pois_geojson(db: Session = Depends(get_db)):
    pois = db.query(PointOfInterest).all()
    features = []
    for p in pois:
        features.append(Feature(
            geometry=GeoPoint((p.lng, p.lat)),
            properties={"id": p.id, "name": p.name, "category": p.category, "description": p.description}
        ))
    return FeatureCollection(features)


@app.post("/api/pois", response_model=POIResponse)
def create_poi(data: POICreate, db: Session = Depends(get_db)):
    poi = PointOfInterest(
        name=data.name,
        category=data.category,
        description=data.description,
        lng=data.lng,
        lat=data.lat,
        geom=f"SRID=4326;POINT({data.lng} {data.lat})"
    )
    db.add(poi)
    db.commit()
    db.refresh(poi)
    return poi


@app.delete("/api/pois/{poi_id}")
def delete_poi(poi_id: int, db: Session = Depends(get_db)):
    poi = db.query(PointOfInterest).filter(PointOfInterest.id == poi_id).first()
    if not poi:
        raise HTTPException(status_code=404, detail="POI not found")
    db.delete(poi)
    db.commit()
    return {"detail": "deleted"}


# ---------- Region endpoints ----------

@app.get("/api/regions/geojson")
def list_regions_geojson(db: Session = Depends(get_db)):
    rows = db.query(
        Region.id, Region.name, Region.label, Region.description,
        ST_AsGeoJSON(Region.geom).label("geojson")
    ).all()
    features = []
    for r in rows:
        geom = json.loads(r.geojson)
        features.append(Feature(
            geometry=geom,
            properties={"id": r.id, "name": r.name, "label": r.label, "description": r.description}
        ))
    return FeatureCollection(features)


@app.post("/api/regions")
def create_region(data: RegionCreate, db: Session = Depends(get_db)):
    geojson_str = json.dumps(data.geojson)
    region = Region(
        name=data.name,
        label=data.label,
        description=data.description,
        geom=f"SRID=4326;{geojson_str}"
    )
    db.add(region)
    db.commit()
    db.refresh(region)
    return {"id": region.id, "name": region.name}


@app.get("/api/health")
def health():
    return {"status": "ok"}