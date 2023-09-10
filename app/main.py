from typing import Annotated
from fastapi import FastAPI,HTTPException, status,Request
from .security import api as security
from .security.auth import verify_signature
from .routes import api as routes
from pydantic import BaseModel
from os import getenv

app:FastAPI = FastAPI()

app.include_router(security.router)
app.include_router(routes.router)
