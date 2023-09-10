from typing import Annotated
from fastapi import APIRouter,status,Header

assignment_router:APIRouter = APIRouter()

@assignment_router.get('/assignment',status_code=status.HTTP_200_OK)
def getAssignment():

    

    return 

@assignment_router.post('/assignment',status_code=status.HTTP_201_CREATED)
def postAssignment():

    

    return 

@assignment_router.put('/assignment',status_code=status.HTTP_205_RESET_CONTENT)
def putAssignment():

    

    return 

@assignment_router.delete('/assignment',status_code=status.HTTP_204_NO_CONTENT)
def deleteAssignment():

    

    return 