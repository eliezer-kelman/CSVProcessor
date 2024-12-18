from pydantic import BaseModel, Field


class Target(BaseModel):
    type: str = Field(..., description="Type of target")

class Attack(BaseModel):
    type: str = Field(..., description="Type of attack")
    target: Target
