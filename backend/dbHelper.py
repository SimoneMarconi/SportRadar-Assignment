import json
import sqlite3
import datetime
from typing import Optional

# helper function to execute queries and get a json formatted result
def executeSQL(conn: sqlite3.Connection, query: str, params: Optional[tuple]):
    if params:
        cursor = conn.execute(query, params)
    else:
        cursor = conn.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    results = [dict(zip(columns, row)) for row in rows]
    return json.dumps(results)

def getAll(conn: sqlite3.Connection):
    query = """SELECT * FROM MATCH_VIEW"""
    res = executeSQL(conn, query, None)
    return res

def filterAfterTime(conn: sqlite3.Connection, date: datetime.date):
    query = """
    SELECT * FROM MATCH_VIEW
    WHERE datetime(date) > datetime(?);
    """
    params = (date, )
    res = executeSQL(conn, query, params)
    return res

def getLeaderBoard(conn: sqlite3.Connection, sportName: Optional[str]):
    if not sportName:
        query = """
        SELECT t.name AS team_name, l.name AS location_name, COUNT(*) AS wins, t.sport AS sport
        FROM TEAM AS t
        JOIN MATCH AS m
            ON (t.team_id = m._team1_id AND m.score_team1 >= m.score_team2 AND m.live = false)
            OR (t.team_id = m._team2_id AND m.score_team2 >= m.score_team1 AND m.live = false)
        JOIN LOCATION AS l
        ON t._location_id = l.location_id
        GROUP BY t.team_id
        ORDER BY wins DESC;
        """ 
        res = executeSQL(conn, query, None)
        return res
    else:
        query = """
        SELECT t.name AS team_name, l.name AS location_name, COUNT(*) AS wins
        FROM TEAM AS t
        JOIN MATCH AS m
            ON (t.team_id = m._team1_id AND m.score_team1 >= m.score_team2 AND m.live = false)
            OR (t.team_id = m._team2_id AND m.score_team2 >= m.score_team1 AND m.live = false)
        JOIN LOCATION AS l
        ON t._location_id = l.location_id
        WHERE t.sport = (?)
        GROUP BY t.team_id
        ORDER BY wins DESC;
        """ 
        params = (sportName, )
        res = executeSQL(conn, query, params)
        return res

def getLiveMatches(conn: sqlite3.Connection, sport: Optional[str]):
    res = None
    if sport:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE live = true AND sport = (?)
        """ 
        params = (sport, )
        res = executeSQL(conn, query, params)
    else:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE live = true
        """ 
        res = executeSQL(conn, query, None)
    return res

def insertMatch(conn: sqlite3.Connection, team1: int, team2: int, location: int, date: str, time: str, description: str, tickets_sold: int):
    query = """
    INSERT INTO MATCH (date, time, _team1_id, _team2_id, _location_id, description, tickets_sold, score_team1, score_team2, live) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """ 
    params = (date, time, team1, team2, location, description, tickets_sold, None, None, False)
    cursor = conn.execute(query, params)
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False

