from typing import Annotated
from fastapi import APIRouter,status
from .schemas import StudentGrades

student_grades_router:APIRouter = APIRouter(
    prefix='/grades'
)

@student_grades_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getGrades():
    return StudentGrades()

@student_grades_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postGrades():
    return StudentGrades()

@student_grades_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putGrades():
    return StudentGrades()

@student_grades_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteGrades():
    return StudentGrades()
