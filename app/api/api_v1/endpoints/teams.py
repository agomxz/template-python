from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session


from api import deps
from schemas import TeamBase, TeamCreate
from crud import team as CRUDTeam


router = APIRouter()


@router.post("/")
def create_team(team_in: TeamCreate,  db: Session = Depends(deps.get_db) ) -> Any:

    """
    Create new team.
    """
    team = CRUDTeam.create(db, obj_in=team_in)
    return team



