from typing import Annotated
from fastapi import APIRouter,Header
from ...security.auth import verify_scope,verify_signature
from ...security.scope import GradeScope
from .types import StudentGrades
from os import getenv

router:APIRouter = APIRouter(prefix=f"/{getenv('API_VERSION')}/onesti")    

@router.get('/grades')
def getGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_READ_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.post('/grades')
def postGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_CREATE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.put('/grades')
def putGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_UPDATE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()

@router.delete('/grades')
def deleteGrades(access_token:Annotated[str,Header()]):

    scopes:list[GradeScope] = [
        GradeScope.USER_DELETE_GRADES.name
    ]

    verify_signature(access_token)
    verify_scope(access_token,scopes)

    return StudentGrades()