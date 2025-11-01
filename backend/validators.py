import json
import sqlite3
import datetime
from dbHelper import executeSQL

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

def isFutureDate(date: str):
    today = datetime.datetime.now()
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date.date() > today.date()