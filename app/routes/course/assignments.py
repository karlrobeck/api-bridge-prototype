from typing import Annotated
from fastapi import APIRouter,status
from .schemas import CourseAssignments

course_assignments_router:APIRouter = APIRouter(
    prefix='/assignments'
)

@course_assignments_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getAssignments():
    return CourseAssignments()

@course_assignments_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postAssignments():
    return CourseAssignments()

@course_assignments_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putAssignments():
    return CourseAssignments()

@course_assignments_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteAssignments():
    return CourseAssignments()
