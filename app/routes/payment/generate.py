from typing import Annotated
from fastapi import APIRouter,status
from .schemas import PaymentGenerate

payment_generate_router:APIRouter = APIRouter(
    prefix='/generate'
)

@payment_generate_router.get(
    '/',
    status_code=status.HTTP_200_OK
)
def getGenerate() -> PaymentGenerate:
    return PaymentGenerate()

@payment_generate_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
def postGenerate() -> PaymentGenerate:
    return PaymentGenerate()

@payment_generate_router.put(
    '/',
    status_code=status.HTTP_205_RESET_CONTENT
)
def putGenerate() -> PaymentGenerate:
    return PaymentGenerate()

@payment_generate_router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def deleteGenerate():
    return PaymentGenerate()
