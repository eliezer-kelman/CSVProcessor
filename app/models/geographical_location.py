from pydantic import BaseModel, Field
from typing import Optional


class Coordinates(BaseModel):
    latitude: Optional[float] = Field(None, ge=-90, le=90, description="Latitude of the event")
    longitude: Optional[float] = Field(None, ge=-180, le=180, description="Longitude of the event")

class Location(BaseModel):
    country: str = Field(..., min_length=1, description="Country name")
    region: str = Field(..., description="Region name")
    province: Optional[str] = Field(None, description="State or province")
    city: Optional[str] = Field(None, description="City name")
    coordinates: Optional[Coordinates] = Field(None, description="Geographical coordinates")
