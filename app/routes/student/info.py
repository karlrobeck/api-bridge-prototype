from typing import Annotated
from fastapi import APIRouter,status
from .schemas import StudentInfo

student_info_router:APIRouter = APIRouter(
    prefix='/info'
)

@student_info_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getInfo() -> StudentInfo:
    return StudentInfo()

@student_info_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postInfo() -> StudentInfo:
    return StudentInfo()

@student_info_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putInfo() -> StudentInfo:
    return StudentInfo()

@student_info_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteInfo():
    return StudentInfo()
