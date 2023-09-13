from fastapi import APIRouter,Depends
from .course import api as course
from .student import api as student
from .news import api as news
from ..security.auth import verify_access_token
from os import getenv

router:APIRouter = APIRouter(
    prefix=f"/{getenv('API_VERSION')}",
    dependencies=[Depends(verify_access_token)]
)
router.include_router(course.router)
router.include_router(student.router)
router.include_router(news.router)

