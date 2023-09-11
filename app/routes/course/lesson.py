from typing import Annotated
from fastapi import APIRouter,status
from .schemas import CourseLesson

course_lesson_router:APIRouter = APIRouter(
    prefix='/lesson'
)

@course_lesson_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getLesson() -> CourseLesson:
    return CourseLesson()

@course_lesson_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postLesson() -> CourseLesson:
    return CourseLesson()

@course_lesson_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putLesson() -> CourseLesson:
    return CourseLesson()

@course_lesson_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteLesson():
    return CourseLesson()
