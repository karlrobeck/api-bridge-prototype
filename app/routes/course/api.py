from fastapi import APIRouter
from .info import info_router
from .assignments import assignment_router
from .activity import activity_router
from .lesson import lesson_router
from .quiz import quiz_router
from .task_performance import task_performance_router

router:APIRouter = APIRouter()
router.include_router(info_router)
router.include_router(assignment_router)
router.include_router(activity_router)
router.include_router(quiz_router)
router.include_router(lesson_router)
router.include_router(task_performance_router)