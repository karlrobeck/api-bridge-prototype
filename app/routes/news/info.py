
from typing import Annotated
from fastapi import APIRouter,status
from .schemas import NewsInfo

news_info_router:APIRouter = APIRouter(
    prefix='/info'
)

@news_info_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getNews() -> NewsInfo:
    return NewsInfo()

@news_info_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postNews() -> NewsInfo:
    return NewsInfo()

@news_info_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putNews() -> NewsInfo:
    return NewsInfo()

@news_info_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteNews():
    return NewsInfo()
