from pydantic import BaseModel

class CourseQuiz(BaseModel):
    title:str=""
    content:list[dict] = [
        {
            'question':'',
            'answer':'',
        }
    ]
    score:int=0

class CourseTaskPerformance(BaseModel):
    title:str=""
    content:str=""
    score:int=0

class CourseAssignments(BaseModel):
    title:str=""
    content:str=""
    score:int=0

class CourseActivity(BaseModel):
    title:str=""
    content:str=""
    score:int=0
    
class CourseLesson(BaseModel):
    title:str=""
    content:str=""
    progress:str=""

class CourseInfo(BaseModel):
    name:str=""
    description:str=""
    contents:dict = {
        'quiz':[
            CourseQuiz(),
        ],
        'task_performance':[
            CourseTaskPerformance(),
        ],
        'assignments':[
            CourseAssignments(),
        ],
        'activities':[
            CourseActivity(),
        ],
        'lessons':[
            CourseLesson(),
        ],
    }
    