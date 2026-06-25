from pydantic import BaseModel
from typing import Optional


class POICreate(BaseModel):
    name: str
    category: str
    description: str = ""
    lng: float
    lat: float


class POIResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str
    lng: float
    lat: float

    class Config:
        from_attributes = True


class RegionCreate(BaseModel):
    name: str
    label: str = ""
    description: str = ""
    geojson: dict


class RegionResponse(BaseModel):
    id: int
    name: str
    label: str
    description: str

    class Config:
        from_attributes = True