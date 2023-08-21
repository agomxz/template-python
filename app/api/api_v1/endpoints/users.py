from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session


from api import deps
from models import user
from schemas import UserCreate, UserUpdate, User
from crud import user as CRUDuser


router = APIRouter()


@router.get("/")
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = CRUDuser.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/")
def create_user( user_in: UserCreate,  db: Session = Depends(deps.get_db) ) -> Any:

    """
    Create new user.
    """
    user = CRUDuser.create(db, obj_in=user_in)
    return user



@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: UserUpdate,
) -> Any:
    """
    Update a user.
    """

    print('Buscando usuario .....')
    user = CRUDuser.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = CRUDuser.update(db, db_obj=user, obj_in=user_in)
    return user