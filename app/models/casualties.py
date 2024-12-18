from pydantic import BaseModel, Field
from typing import Optional


class Casualties(BaseModel):
    killed: Optional[int] = Field(None, ge=0, description="Number of people killed")
    killed_terrorists: Optional[int] = Field(None, ge=0, description="Number of terrorists killed")
    wounded: Optional[int] = Field(None, ge=0, description="Number of people wounded")
    wounded_terrorists: Optional[int] = Field(None, ge=0, description="Number of terrorists wounded")
