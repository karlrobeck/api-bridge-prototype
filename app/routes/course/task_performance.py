from typing import Annotated
from fastapi import APIRouter,status,Header

task_performance_router:APIRouter = APIRouter()

@task_performance_router.get('/task_performance',status_code=status.HTTP_200_OK)
def getTaskPerformance():

    

    return 

@task_performance_router.post('/task_performance',status_code=status.HTTP_201_CREATED)
def postTaskPerformance():

    

    return 

@task_performance_router.put('/task_performance',status_code=status.HTTP_205_RESET_CONTENT)
def putTaskPerformance():

    

    return 

@task_performance_router.delete('/task_performance',status_code=status.HTTP_204_NO_CONTENT)
def deleteTaskPerformance():

    

    return 