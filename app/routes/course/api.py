from fastapi import APIRouter
from os import getenv

router:APIRouter = APIRouter(prefix=f"/{getenv('API_VERSION')}/course")