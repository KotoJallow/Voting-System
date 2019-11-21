import sqlite3 as sqlite
import DBQueries


connection = sqlite.connect('data.db')
connection.row_factory = sqlite.Row  # Enables accessing columns via names
database = connection.cursor()

def getLogin(username,password):
    result = database.execute(DBQueries.getLogin,(username,password)).fetchall()
    if(len(result) == 1):
        return result[0]['Id']
    return False

print(getLogin('1234','1234'))


def getContestant(id):
    query = DBQueries.getContestant % id
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def getNamesOfAllContestants():
    result = database.execute(DBQueries.getNamesOfAllContestants).fetchall()
    names = []
    for name in result:
        names.append(name[0])
    return names

def getContestantNameParty():
    result = database.execute(DBQueries.getContestantNameParty).fetchall()
    namesParty = []
    for nameParty in result:
        namesParty.append(dict(nameParty))
    return namesParty

def getParty(id):
    query = DBQueries.getParty % id
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def getUser(id):
    query = DBQueries.getUser % id
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def getVotes(id):
    query = DBQueries.getVotes % id
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def getTotalVotes():
    query = DBQueries.getTotalVotes
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def getWinner():
    query = DBQueries.getWinner
    result = database.execute(query).fetchone()
    if result:
        return dict(result)
    return False

def insertUser(firstname,middlename,lastname,idnumber,gender,password):
    try:
        database.execute(DBQueries.insertUser,(firstname,middlename,lastname,idnumber,gender,password))
        connection.commit()
        return True
    except:
        return False

# Sqlite is crazy ; allows strings for Integer. Fix on UI
def insertVote(user,contestant):
    try:
        database.execute(DBQueries.insertVote,(user,contestant));
        connection.commit()
        return True
    except:
        return False

#connection.close()