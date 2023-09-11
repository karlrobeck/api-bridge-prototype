from fastapi import APIRouter, Depends
from .info import course_info_router
from .assignments import course_assignments_router
from .activity import course_activity_router
from .lesson import course_lesson_router
from .quiz import course_quiz_router
from .task_performance import course_task_performance_router

router:APIRouter = APIRouter(
    prefix='/course',
    tags=['course'],
)
router.include_router(course_info_router)
router.include_router(course_assignments_router)
router.include_router(course_activity_router)
router.include_router(course_quiz_router)
router.include_router(course_lesson_router)
router.include_router(course_task_performance_router)