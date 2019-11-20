import sqlite3 as sqlite
import os
import DBQueries



path = os.path.dirname(os.path.abspath(__file__))
databasePath = os.path.join(path, './db/data.db')

connection = sqlite.connect('data.db')
database = connection.cursor()

def userExist(username,password):
    result = database.execute('''select * from user''')
    if(len(result.fetchall()) > 0):
        for d in result:
            print(25)
    return -98

userExist(1234,1234)

database.close()