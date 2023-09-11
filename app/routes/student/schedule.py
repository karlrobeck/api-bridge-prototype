from typing import Annotated
from fastapi import APIRouter,status
from .schemas import StudentSchedule

student_schedule_router:APIRouter = APIRouter(
    prefix='/schedule'
)

@student_schedule_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getSchedule():
    return StudentSchedule()

@student_schedule_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postSchedule():
    return StudentSchedule()

@student_schedule_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putSchedule():
    return StudentSchedule()

@student_schedule_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteSchedule():
    return StudentSchedule()
