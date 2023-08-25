from typing import Any
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.user import Team, UserTeam
from schemas.team import TeamBase, TeamCreate, TeamUpdate


class CRUDTeam(CRUDBase[TeamBase, TeamCreate, TeamUpdate]):

    def create(self, db: Session, *, obj_in: TeamCreate) -> Team:
        db_obj = Team(
            name = obj_in.name,
            description = obj_in.description,
            logo = obj_in.logo,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def add_player(self, db: Session, *, team_id: int, player_id: int) -> Any:
        db_obj = UserTeam(
            team_id = team_id,
            user_id = player_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

team = CRUDTeam(Team)