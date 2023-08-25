from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from schemas import MatchBase, MatchCreate, MatchUpdate
from crud import match as CRUDMatch


router = APIRouter()

@router.post("/")
def create_match(team_in: MatchCreate,  db: Session = Depends(deps.get_db)) -> Any:
    """
    Create new match.
    """
    team = CRUDMatch.create(db=db, obj_in=team_in)
    return team