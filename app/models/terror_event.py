from pydantic import BaseModel, Field

from app.models.attack_and_target import Attack
from app.models.attackers import Attackers
from app.models.casualties import Casualties
from app.models.geographical_location import Location


class TerrorEvent(BaseModel):
    eventid: int = Field(..., description="Unique identifier for the event")
    date: dict = Field(..., description="Event date details")  # שנה, חודש, יום
    location: Location
    casualties: Casualties
    attack: Attack
    attackers: Attackers

    # Validators
    @staticmethod
    def validate_date(data):
        """Ensure year, month, and day are valid."""
        year = data.get("year")
        month = data.get("month", 1)  # Default to January
        day = data.get("day", 1)  # Default to 1st day
        return {"year": year, "month": month, "day": day}
