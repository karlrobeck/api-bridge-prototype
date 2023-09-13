from pydantic import BaseModel

class StudentBalance(BaseModel):
    title:str=""
    current_balance:float=0.0
    contents:dict = {
        'prelim':0.0,
        'midterm':0.0,
        'prefinal':0.0,
        'final':0.0,
    }

class StudentGrades(BaseModel):
    title:str=""
    contents:dict = {
        'prelim':0,
        'midterm':0,
        'prefinal':0,
        'final':0,
    }

class StudentSchedule(BaseModel):
    title:str=""
    contents:str= [
        {'subject':'','time':''}
    ]

class StudentInfo(BaseModel):
    title:str=""
    description:str=""
    contents:dict = {
        'balance':StudentBalance(),
        'grades':StudentGrades(),
        'schedule':StudentSchedule(),
    }
    