from fastapi import APIRouter,Depends
from .course import api as course
from os import getenv
from ..security.auth import verify_request
router:APIRouter = APIRouter(
    prefix=f"/{getenv('API_VERSION')}/course",
    tags=['course'],
    dependencies=[Depends(verify_request)]
)
router.include_router(course.router)
