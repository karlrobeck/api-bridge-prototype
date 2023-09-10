from enum import Enum


class GradeScope(Enum):
    """
    Scopes for accessing grades.

    USER_READ_GRADES: Read grades.
    USER_UPDATE_GRADES: Update grades.
    USER_CREATE_GRADES: Create grades.
    USER_DELETE_GRADES: Delete grades.
    """

    USER_READ_GRADES = 1
    USER_UPDATE_GRADES = 2
    USER_CREATE_GRADES = 3
    USER_DELETE_GRADES = 4


class ScheduleScope(Enum):
    """
    Scopes for accessing schedules.

    USER_READ_SCHEDULE: Read schedules.
    USER_UPDATE_SCHEDULE: Update schedules.
    USER_CREATE_SCHEDULE: Create schedules.
    USER_DELETE_SCHEDULE: Delete schedules.
    """

    USER_READ_SCHEDULE = 5
    USER_UPDATE_SCHEDULE = 6
    USER_CREATE_SCHEDULE = 7
    USER_DELETE_SCHEDULE = 8


class CurriculumScope(Enum):
    """
    Scopes for accessing curriculums.

    USER_READ_CURRICULUM: Read curriculums.
    USER_UPDATE_CURRICULUM: Update curriculums.
    USER_CREATE_CURRICULUM: Create curriculums.
    USER_DELETE_CURRICULUM: Delete curriculums.
    """

    USER_READ_CURRICULUM = 9
    USER_UPDATE_CURRICULUM = 10
    USER_CREATE_CURRICULUM = 11
    USER_DELETE_CURRICULUM = 12


class ClassroomScope(Enum):
    """
    Scopes for accessing classrooms.

    USER_READ_CLASSROOM: Read classrooms.
    USER_UPDATE_CLASSROOM: Update classrooms.
    USER_CREATE_CLASSROOM: Create classrooms.
    USER_DELETE_CLASSROOM: Delete classrooms.
    """

    USER_READ_CLASSROOM = 13
    USER_UPDATE_CLASSROOM = 14
    USER_CREATE_CLASSROOM = 15
    USER_DELETE_CLASSROOM = 16


class NewsScope(Enum):
    """
    Scopes for accessing news.

    USER_READ_NEWS: Read news.
    USER_UPDATE_NEWS: Update news.
    USER_CREATE_NEWS: Create news.
    USER_DELETE_NEWS: Delete news.
    """

    USER_READ_NEWS = 17
    USER_UPDATE_NEWS = 18
    USER_CREATE_NEWS = 19
    USER_DELETE_NEWS = 20


class StudentSectionScope(Enum):
    """
    Scopes for accessing student sections.

    USER_READ_STUDENT_SECTION: Read student sections.
    USER_UPDATE_STUDENT_SECTION: Update student sections.
    USER_CREATE_STUDENT_SECTION: Create student sections.
    USER_DELETE_STUDENT_SECTION: Delete student sections.
    """

    USER_READ_STUDENT_SECTION = 21
    USER_UPDATE_STUDENT_SECTION = 22
    USER_CREATE_STUDENT_SECTION = 23
    USER_DELETE_STUDENT_SECTION = 24