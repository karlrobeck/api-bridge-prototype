from typing import Annotated
from fastapi import APIRouter,status
from .schemas import CourseActivity

course_activity_router:APIRouter = APIRouter(
    prefix='/activity'
)

@course_activity_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getActivity():
    return CourseActivity()

@course_activity_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postActivity():
    return CourseActivity()

@course_activity_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putActivity():
    return CourseActivity()

@course_activity_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteActivity():
    return CourseActivity()
