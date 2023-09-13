from fastapi import APIRouter
from .generate import payment_generate_router

router:APIRouter = APIRouter(
    prefix='/payment',
    tags=['payment'],
)
router.include_router(payment_generate_router)
