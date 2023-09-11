from typing import Annotated
from fastapi import APIRouter,status
from .schemas import CourseTaskPerformance

course_task_performance_router:APIRouter = APIRouter(
    prefix='/task_performance'
)

@course_task_performance_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getTaskPerformance():
    return CourseTaskPerformance()

@course_task_performance_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postTaskPerformance():
    return CourseTaskPerformance()

@course_task_performance_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putTaskPerformance():
    return CourseTaskPerformance()

@course_task_performance_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteTaskPerformance():
    return CourseTaskPerformance()
