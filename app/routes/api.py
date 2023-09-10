from fastapi import APIRouter
from .course import api as course

router:APIRouter = APIRouter()
router.include_router(course.router)
