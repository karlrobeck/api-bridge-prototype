from typing import Annotated
from fastapi import APIRouter,status,Header

quiz_router:APIRouter = APIRouter()

@quiz_router.get('/quiz',status_code=status.HTTP_200_OK)
def getQuiz():

    

    return 

@quiz_router.post('/quiz',status_code=status.HTTP_201_CREATED)
def postQuiz():

    

    return 

@quiz_router.put('/quiz',status_code=status.HTTP_205_RESET_CONTENT)
def putQuiz():

    

    return 

@quiz_router.delete('/quiz',status_code=status.HTTP_204_NO_CONTENT)
def deleteQuiz():

    

    return 