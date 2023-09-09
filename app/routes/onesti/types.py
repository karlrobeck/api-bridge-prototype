from pydantic import BaseModel

class SubjectGrades(BaseModel):
    prelim:float=0.0
    midterms:float=0.0
    prefinals:float=0.0
    finals:float=0.0

class StudentGrades(BaseModel):
    subject:str=""
    instructor:str=""
    date_released:str=""
    data:SubjectGrades = SubjectGrades(
        prelim=0.0,
        midterms=0.0,
        prefinals=0.0,
        finals=0.0
    )