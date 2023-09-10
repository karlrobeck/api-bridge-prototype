from typing import Annotated
from fastapi import APIRouter,status,Header

lesson_router:APIRouter = APIRouter()

@lesson_router.get('/lesson',status_code=status.HTTP_200_OK)
def getLesson():

    

    return 

@lesson_router.post('/lesson',status_code=status.HTTP_201_CREATED)
def postLesson():

    

    return 

@lesson_router.put('/lesson',status_code=status.HTTP_205_RESET_CONTENT)
def putLesson():

    

    return 

@lesson_router.delete('/lesson',status_code=status.HTTP_204_NO_CONTENT)
def deleteLesson():

    

    return 