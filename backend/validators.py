import json
import sqlite3
import datetime
from dbHelper import executeSQL

# check if a team name is in the database and return it's id
def checkTeam(conn: sqlite3.Connection, team_name: str):
    query = """
    SELECT team_id FROM TEAM
    WHERE name = (?)
    """ 
    params = (team_name, )
    res = executeSQL(conn, query, params)
    d = json.loads(res)
    if len(d) == 0:
        return None
    return d[0]["team_id"]

# check if the sport of the two teams provided is the same
def checkSports(conn:sqlite3.Connection, team_name1: str, team_name2: str):
    query = """
    SELECT COUNT(DISTINCT sport) AS total FROM TEAM
    WHERE name = (?) OR name = (?)
    """ 
    params = (team_name1, team_name2)
    res = executeSQL(conn, query, params)
    d = json.loads(res)
    if len(d) == 0:
        return None
    if d[0]["total"] > 1:
        return False
    else:
        return True


# check if the location provided exists in the database
def checkLocation(conn: sqlite3.Connection, location_name: str):
    query = """
    SELECT location_id FROM LOCATION
    WHERE name = (?)
    """ 
    params = (location_name, )
    res = executeSQL(conn, query, params)
    d = json.loads(res)
    if len(d) == 0:
        return None
    return d[0]["location_id"]

# check if the data provided is a future date
def isFutureDate(date: str):
    try:
        input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return False
    today = datetime.date.today()
    return input_date > today
