from typing import Annotated
from fastapi import FastAPI, Depends,HTTPException, status
from sti.security import api
from pydantic import BaseModel

app:FastAPI = FastAPI()

app.include_router(api.router)