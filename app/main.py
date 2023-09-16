from typing import Annotated
from fastapi import FastAPI,HTTPException, status,Request
from fastapi.staticfiles import StaticFiles
from .security import api as security
from .security.auth import verify_signature
from .routes import api as routes
from pydantic import BaseModel
from os import getenv
from fastapi.middleware.cors import CORSMiddleware

app:FastAPI = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(security.router)
app.include_router(routes.router)
