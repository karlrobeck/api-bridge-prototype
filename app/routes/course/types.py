from pydantic import BaseModel

class Quiz(BaseModel):
    title:str=""
    content:list[dict] = [
        {
            'question':'',
            'answer':'',
        }
    ]
    score:int

class TaskPerformance(BaseModel):
    title:str=""

class Assignments(BaseModel):
    title:str=""

class Activity(BaseModel):
    title:str=""
    
class CourseLesson(BaseModel):
    title:str=""
    contents:list[list[Quiz | TaskPerformance | Assignments | Activity]] = [
        [
            Quiz(),
            TaskPerformance(),
            Assignments(),
            Activity(),
        ]
    ]

class CourseInfo(BaseModel):
    name:str
    description:str
    