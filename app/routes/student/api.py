from fastapi import APIRouter, Depends
from .balance import student_balance_router
from .grades import student_grades_router
from .info import student_info_router
from .schedule import student_schedule_router

router:APIRouter = APIRouter(
    prefix='/student',
    tags=['student'],
)
router.include_router(student_info_router)
router.include_router(student_balance_router)
router.include_router(student_grades_router)
router.include_router(student_schedule_router)