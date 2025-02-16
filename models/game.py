from pydantic import BaseModel, Field
from datetime import datetime

class Game(BaseModel):
    time: datetime = Field(...)
    field: int = Field(..., gt=0, lt=4)
    color: str = Field(...)
    team: str = Field(None)
    subs_needed: int = Field(None)