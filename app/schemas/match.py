from typing import Optional
from pydantic import BaseModel


# Shared properties
class MatchBase(BaseModel):
    team_local: Optional[int] = None
    team_visitor: Optional[int] = None
    date: Optional[str] = None
    score_local: Optional[int] = None
    score_visitor: Optional[int] = None
    stadium_id: Optional[int] = None

class MatchCreate(MatchBase):
    pass

class MatchUpdate(MatchBase):
    pass