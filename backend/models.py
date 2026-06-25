from sqlalchemy import Column, Integer, String, Float, Text
from geoalchemy2 import Geometry
from database import Base


class PointOfInterest(Base):
    __tablename__ = "points_of_interest"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, default="")
    lng = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
    geom = Column(Geometry(geometry_type="POINT", srid=4326))


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    label = Column(String(100), default="")
    description = Column(Text, default="")
    geom = Column(Geometry(geometry_type="POLYGON", srid=4326))