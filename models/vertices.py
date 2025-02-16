from enum import Enum
from typing import ClassVar
from pydantic import BaseModel, Field, EmailStr

class VertexType(str, Enum):
    PLAYER = "Player"
    TEAM = "Team"

class Player(BaseModel):
    label: ClassVar[VertexType] = VertexType.PLAYER
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone: str = Field(...)
    email: EmailStr = Field(...)

class PlayerUpdate(BaseModel):
    first_name: str = Field(None)
    last_name: str = Field(None)
    phone: str = Field(None)
    email: EmailStr = Field(None)

class Team(BaseModel):
    label:ClassVar[VertexType] = VertexType.TEAM
    name: str = Field(...)
    division: int = Field(..., gt=0, lt=100)

class TeamUpdate(BaseModel):
    name: str|None = Field(None)
    division: str|None = Field(None)

def all_fields_none(instance: BaseModel) -> bool:
    return all(value is None for value in instance.model_dump().values())