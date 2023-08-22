from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class TeamBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API on creation
class TeamCreate(TeamBase):
    description: str
    logo: str
    #city: str
    #country: str
    #league: str
    coach: str
    president: str


# Properties to receive via API on creation
class TeamUpdate(TeamBase):
    description: str
