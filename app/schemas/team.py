from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class TeamBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API on creation
class TeamCreate(TeamBase):
    pass


# Properties to receive via API on creation
class TeamUpdate(TeamBase):
    email: EmailStr
