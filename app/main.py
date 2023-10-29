from fastapi import FastAPI
from api.api_v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TEAMS")

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
