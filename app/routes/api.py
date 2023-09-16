from fastapi import APIRouter,Depends
from .course import api as course
from .student import api as student
from .news import api as news
from .payment import api as payment
from .application import api as application
from app.security.auth import verify_access_token,verify_admin
from os import getenv

router:APIRouter = APIRouter(
    prefix=f"/{getenv('API_VERSION')}",
)
router.include_router(application.router,dependencies=[Depends(verify_admin)])
router.include_router(course.router,dependencies=[Depends(verify_access_token)])
router.include_router(student.router,dependencies=[Depends(verify_access_token)])
router.include_router(news.router,dependencies=[Depends(verify_access_token)])
router.include_router(payment.router,dependencies=[Depends(verify_access_token)])

