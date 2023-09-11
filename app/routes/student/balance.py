from typing import Annotated
from fastapi import APIRouter,status
from .schemas import StudentBalance

student_balance_router:APIRouter = APIRouter(
    prefix='/balance'
)

@student_balance_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getBalance():
    return StudentBalance()

@student_balance_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postBalance():
    return StudentBalance()

@student_balance_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putBalance():
    return StudentBalance()

@student_balance_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteBalance():
    return StudentBalance()
