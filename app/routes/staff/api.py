from fastapi import APIRouter

router:APIRouter = APIRouter(
    prefix='/staff',
    tags=['staff'],
)