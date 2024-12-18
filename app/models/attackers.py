from pydantic import BaseModel, Field
from typing import Optional


class Attackers(BaseModel):
    primary_group: str = Field(..., min_length=1, description="Name of the primary group involved")
    secondary_group: Optional[str] = Field(None, description="Name of the secondary group involved")
    tertiary_group: Optional[str] = Field(None, description="Name of the tertiary group involved")
    perpetrators: Optional[int] = Field(None, ge=0, description="Number of perpetrators")
    captured: Optional[int] = Field(None, ge=0, description="Number of perpetrators captured")
