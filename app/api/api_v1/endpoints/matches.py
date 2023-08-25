from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps
from schemas import MatchBase, MatchCreate, MatchUpdate
from crud import match as CRUDMatch


router = APIRouter()

@router.get("/")
def read_matches(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve matches.
    """
    matches = CRUDMatch.get_multi(db, skip=skip, limit=limit)
    return matches


@router.post("/")
def create_match(team_in: MatchCreate,  db: Session = Depends(deps.get_db)) -> Any:
    """
    Create new match.
    """
    team = CRUDMatch.create(db=db, obj_in=team_in)
    return team


@router.delete("/{match_id}", response_model=MatchBase)
def remove_match(
    *,
    db: Session = Depends(deps.get_db),
    match_id: int,
) -> Any:
    """
    Delete a match.
    """
    match = CRUDMatch.get(db, id=match_id)
    print(match)
    return match
    if not match:
        raise HTTPException(
            status_code=404,
            detail="The match with this id does not exist in the system",
        )
    match = CRUDMatch.remove(db, id=match_id)
    return match