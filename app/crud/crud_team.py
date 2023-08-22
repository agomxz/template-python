from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import Team
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

team = CRUDTeam(Team)