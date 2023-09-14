import sqlite3
import os
import random


def getRecord(table:str):

    connection = sqlite3.connect('sti.db')

    cursor = connection.cursor()

    data = cursor.execute(f"SELECT * FROM {table}")
    
    return data.fetchall()

def putRecord():
    pass

def postRecord(table:str,values:dict):

    values = values.copy()
    
    connection = sqlite3.connect('sti.db')

    cursor = connection.cursor()

    column = ','.join([str(f'"{x}"') for x in test_data.keys()])
    values = ','.join([str(f'"{x}"') for x in test_data.values()])

    cursor.execute(f'INSERT INTO {table} ({column}) VALUES ({values})')
    connection.commit()
    connection.close()
    

def deleteRecord():
    pass

if __name__ == "__main__":
    
    if os.path.exists('sti.db'):
        os.remove('sti.db')
        with open('sti.db','x+') as f:
            pass

    connection = sqlite3.connect('sti.db')

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE User (
            user_id int not null unique,
            username varchar(255) not null,
            password varchar(255) not null,
            first_name varchar(255) not null,
            last_name varchar(255) not null,
            email varchar(255) not null,
            role varchar(255) not null
        )
    """)

    cursor.execute("""
        CREATE TABLE CourseQuiz (
            course_id int not null,
            quiz_id int not null,
            title text not null,
            question text not null,
            answer text not null
        )
    """)

    cursor.execute("""
        CREATE TABLE CourseTaskPerformance (
            course_id int not null,
            task_performance_id int not null unique,
            title text not null,
            description text not null
        )
    """)

    connection.close()

    test_data = {
        "course_id":'1',
        "quiz_id":'1',
        "title":'hello',
        "question":'hello my question',
        "answer":'hello my answer'
    }

    postRecord('CourseQuiz',values=test_data)

    print(getRecord('CourseQuiz'))

    
        
