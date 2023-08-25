from typing import Any
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.user import Match
from schemas.match import MatchBase, MatchCreate, MatchUpdate

class CRUDMatch(CRUDBase[MatchBase, MatchCreate, MatchUpdate]):
    def create(self, db: Session, *, obj_in: MatchCreate) -> Match:
        db_obj = Match(
            team_local = obj_in.team_local,
            team_visitor = obj_in.team_visitor,
            date = obj_in.date,
            score_local = obj_in.score_local,
            score_visitor = obj_in.score_visitor,
            stadium_id = obj_in.stadium_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj





match = CRUDMatch(Match)