from typing import Annotated
from fastapi import APIRouter,status,Header

activity_router:APIRouter = APIRouter()

@activity_router.get('/activity',status_code=status.HTTP_200_OK)
def getActivity():

    return 

@activity_router.post('/activity',status_code=status.HTTP_201_CREATED)
def postActivity():

    return 

@activity_router.put('/activity',status_code=status.HTTP_205_RESET_CONTENT)
def putActivity():

    return 

@activity_router.delete('/activity',status_code=status.HTTP_204_NO_CONTENT)
def deleteActivity():

    return 