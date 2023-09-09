from typing import Annotated
from fastapi import APIRouter,Header,status
from ...security.auth import verify_scope,verify_signature
from ...security.scope import GradeScope
from .types import StudentGrades
from os import getenv

router:APIRouter = APIRouter(prefix=f"/{getenv('API_VERSION')}/onesti")    

@router.get('/grades',status_code=status.HTTP_200_OK)
def getGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_READ_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.post('/grades',status_code=status.HTTP_201_CREATED)
def postGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_CREATE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.put('/grades',status_code=status.HTTP_200_OK)
def putGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_UPDATE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.delete('/grades',status_code=status.HTTP_204_NO_CONTENT)
def deleteGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_DELETE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return 