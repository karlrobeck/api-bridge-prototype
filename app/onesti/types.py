class Grades:

    def __init__(self) -> None:
        self.school_year:str = ''
        self.subject:str = ""
        self.subject:str = ''
        self.instructor:str = ''
        self.release_date:str =''
        self.grades:dict = {
            "prelim":"",
            "midterm":"",
            "prefinals":"",
            "finals":"",
        }

class Schedule:

    def __init__(self) -> None:
        self.subject:str =""
        self.days:str=""
        self.time:str=""
        self.room:str=""
        self.intructor:str=""        

class Curriculum:

    def __init__(self) -> None:
        self.total:int = 0
        self.taken:int = 0
        self.needed:int = self.total - self.taken
        self.subjects:dict = {
            "first_year":{
                "first_term":[],
                "second_term":[],
            },
            "second_year":{
                "first_term":[],
                "second_term":[],
            },
            "third_year":{
                "first_term":[],
                "second_term":[],
            },
            "forth_year":{
                "first_term":[],
                "second_term":[],
            },
            "elective_course":[],
        }

class Balance:
    def __init__(self) -> None:
        self.term:str =''
        self.term_charge:dict = {
            'tuition fee':0,
            'Other School Fees':0,
            'Miscellaneous Fees':0,
        }
        self.payment_schedule:dict = [
            {'date':'','price':0},
            {'date':'','price':0},
            {'date':'','price':0},
            {'date':'','price':0},
        ]
        self.payment:dict = [{
            "date":'',
            "description":'',
            "prices":[],
        }]      
