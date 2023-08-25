from fastapi import APIRouter

from api.api_v1.endpoints import login
from api.api_v1.endpoints import users
from api.api_v1.endpoints import teams
from api.api_v1.endpoints import matches

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(teams.router, prefix="/teams", tags=["teams"])
api_router.include_router(matches.router, prefix="/matches", tags=["matches"])