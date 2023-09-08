from fastapi import APIRouter
from os import getenv
from .types import Grades,Schedule,Curriculum,Balance

router:APIRouter = APIRouter(prefix=f"/{getenv('API_VERSION')}/onesti")

#staff endpoint

#non staff endpoint
@router.get('/grades')
def getGrades(student_id:str):

    student_grades:Grades = Grades()
    student_grades.grades = {
        'prelim':'90',
        'midterm':'90',
        'prefinals':'90',
        'finals':'90',
    }

    return {"data":[student_grades]}

@router.get('/schedules')
def getSchedule(student_id:str,days:str="all"):

    student_schedule = Schedule()

    if days != "all":
        return {"":student_schedule}
    
    return {"":[
        student_schedule,
        student_schedule,
        student_schedule,
        student_schedule,
        student_schedule,
    ]}
@router.get('/curriculum')
def getCurriculum():

    student_curriculum:Curriculum = Curriculum()

    return {"data":student_curriculum}

@router.get('/balance')
def getBalance():

    student_balance:Balance = Balance()

    return {"data":student_balance}
