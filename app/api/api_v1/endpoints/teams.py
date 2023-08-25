from typing import Any
from fastapi import APIRouter, Depends, HTTPException
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


@router.patch("/{team_id}", response_model=TeamBase)
def update_team(
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


@router.delete("/{team_id}", response_model=TeamBase)
def delete_team(
    *,
    db: Session = Depends(deps.get_db),
    team_id: int,
) -> Any:
    """
    Delete a team.
    """
    team = CRUDTeam.get(db, id=team_id)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The team with this id does not exist in the system",
        )
    user = CRUDTeam.remove(db, id=team_id)
    return user



@router.post("/add_player/{team_id}")
def add_player(
    *,
    db: Session = Depends(deps.get_db),
    team_id: int,
    player_id: int,
) -> Any:
    """
    Add a player to a team.
    """
    team = CRUDTeam.get(db, id=team_id)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The team with this id does not exist in the system",
        )
    user = CRUDTeam.add_player(db, team_id=team_id, player_id=player_id)
    return user



@router.delete("/remove_player/{team_id}")
def remove_player(
    *,
    db: Session = Depends(deps.get_db),
    team_id: int,
    player_id: int,
) -> Any:
    """
    Remove a player from a team.
    """
    team = CRUDTeam.get(db, id=team_id)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The team with this id does not exist in the system",
        )
    user = CRUDTeam.remove_player(db, team_id=team_id, player_id=player_id)
    return user