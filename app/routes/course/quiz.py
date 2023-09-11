from typing import Annotated
from fastapi import APIRouter,status
from .schemas import CourseQuiz

course_quiz_router:APIRouter = APIRouter(
    prefix='/quiz'
)

@course_quiz_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getQuiz():
    return CourseQuiz()

@course_quiz_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postQuiz():
    return CourseQuiz()

@course_quiz_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putQuiz():
    return CourseQuiz()

@course_quiz_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteQuiz():
    return CourseQuiz()
