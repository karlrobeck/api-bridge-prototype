import sqlite3

def insertRecord(database:str,table:str,data:dict):
    
    connection = sqlite3.connect(database)

    keys = [f"'{key.upper()}'" for key in data.keys()]
    values = [f"'{value}'" for value in data.values()]

    connection.execute(f"""
        INSERT INTO {table} ({f','.join(keys)}) VALUES ({f','.join(values)})   
    """)
    connection.commit()

    connection.close()
    
    return

def getRecord(database:str,table:str,column:list|None=None,condition:list|None=None):

    connection = sqlite3.connect(database)

    print(f"SELECT {','.join(column) if column else '*'} FROM {table}")
    result = connection.execute(f"""
        SELECT {','.join(column) if column else '*'} FROM {table} {'WHERE ' + ' and '.join(condition) if condition else ''}
    """).fetchall()

    connection.close()

    return result

def updateRecord(database:str,table:str,data_set:dict,condition:list):

    connection = sqlite3.connect(database)

    column = data_set.keys()

    values = [f"'{value}'" for value in data_set.values()]

    connection.execute(f"""
        UPDATE {table} SET {','.join([f'{col} = {val}' for col,val in zip(column,values)])} WHERE {' and '.join(condition)};    
    """)

    connection.commit()
    connection.close()

    return

def checkRecord(database:str,table:str,data_find:list):

    connection = sqlite3.connect(database)

    res = connection.execute(f"""
        SELECT * FROM {table} WHERE ({' and '.join(data_find)})
    """).fetchall()

    connection.close()

    if not res:
        return False
    return True

def createTable(database:str,name:str):

    connection = sqlite3.connect(database)

    connection.execute(f"""
        CREATE TABLE {name} (
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL UNIQUE,
            DESCRIPTION TEXT NOT NULL  
        );
    """)

    connection.close()

def tableSize(database:str,table):

    connection = sqlite3.connect(database)

    res = connection.execute(f"""SELECT COUNT(*) {table}""").fetchone()[0]

    connection.close()
    return res

if __name__ == "__main__":
    
    Database_path = 'test.db'

    with open ('tables.sql','r') as script:
        
        connection = sqlite3.connect(Database_path)
        
        connection.executescript(script.read())
        print(script.read())
        print('SCRIPT EXECUTED')
        
        connection.close()

    print(getRecord(Database_path,'APP',condition=["NAME = 'KARL'"]))
    updateRecord(Database_path,'APP',{'DESCRIPTION':'DEVELOPER'},condition=["NAME = 'VIVIEN'"])
    print(getRecord(Database_path,'APP',condition=["NAME = 'KARL'"]))
    print(getRecord(Database_path,'APP'))
    print(checkRecord(Database_path,'APP',["NAME = 'james'"]))