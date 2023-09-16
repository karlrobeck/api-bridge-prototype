from fastapi import APIRouter
from .register import app_register_router
from .info import application_info_router

router:APIRouter = APIRouter(
    prefix='/application',
    tags=['application'],
)

router.include_router(app_register_router)
router.include_router(application_info_router)