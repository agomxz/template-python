from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session


from api import deps
from schemas import TeamBase, TeamCreate, TeamUpdate
from crud import team as CRUDTeam


router = APIRouter()


@router.post("/")
def create_team(team_in: TeamCreate,  db: Session = Depends(deps.get_db)) -> Any:
    """
    Create new team.
    """
    team = CRUDTeam.create(db, obj_in=team_in)
    return team


@router.get("/")
def read_team(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve team.
    """
    team = CRUDTeam.get_multi(db, skip=skip, limit=limit)
    return team


@router.put("/{team_id}", response_model=TeamBase)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    team_id: int,
    team_in: TeamUpdate,
) -> Any:
    """
    Update a team.
    """
    team = CRUDTeam.get(db, id=team_id)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The team with this id does not exist in the system",
        )
    user = CRUDTeam.update(db, db_obj=team, obj_in=team_in)
    return user



