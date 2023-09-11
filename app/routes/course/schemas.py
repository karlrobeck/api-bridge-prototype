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

class CourseAssignments(BaseModel):
    title:str=""

class CourseActivity(BaseModel):
    title:str=""
    
class CourseLesson(BaseModel):
    title:str=""
    contents:list[list[CourseQuiz | CourseTaskPerformance | CourseAssignments | CourseActivity]] = [
        [
            CourseQuiz(),
            CourseTaskPerformance(),
            CourseAssignments(),
            CourseActivity(),
        ]
    ]

class CourseInfo(BaseModel):
    name:str=""
    description:str=""
    