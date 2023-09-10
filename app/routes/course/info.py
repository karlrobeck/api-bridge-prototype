from typing import Annotated
from fastapi import APIRouter,status,Header

info_router:APIRouter = APIRouter()

@info_router.get('/info',status_code=status.HTTP_200_OK)
def getCourseInfo():

    

    return 

@info_router.post('/info',status_code=status.HTTP_201_CREATED)
def postCourseInfo():

    

    return 

@info_router.put('/info',status_code=status.HTTP_205_RESET_CONTENT)
def putCourseInfo():

    

    return 

@info_router.delete('/info',status_code=status.HTTP_204_NO_CONTENT)
def deleteCourseInfo():

    

    return 