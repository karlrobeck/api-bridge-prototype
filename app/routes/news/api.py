from fastapi import APIRouter
from .info import news_info_router

router:APIRouter = APIRouter(
    prefix='/news',
    tags=['news'],
)
router.include_router(news_info_router)