from typing import List
from pydantic import Field, BaseModel

class Location(BaseModel):
    type: str = Field(default="Point")
    coordinates: List[float] = Field(default=[])