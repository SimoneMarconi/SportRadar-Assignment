import json
import sqlite3
import datetime
from typing import Optional


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
    executeSQL(conn, query, params)
    return 

def filterTeamName(conn: sqlite3.Connection, teamName: str):
    query = """
    SELECT * FROM MATCH_VIEW
    WHERE team1 == (?) OR team2 == (?);
    """
    params = (teamName, teamName)
    res = executeSQL(conn, query, params)
    return res

def filterSportName(conn: sqlite3.Connection, sportName: str):
    query = """
    SELECT v.*
    FROM MATCH AS m
    JOIN MATCH_VIEW AS v 
      ON m.match_id = v.match_id
    JOIN TEAM AS t
      ON t.team_id IN (m.team1_id, m.team2_id)
    WHERE t.sport = (?)
    GROUP BY(v.match_id);
    """
    params =  (sportName, )
    res = executeSQL(conn, query, params)
    return res

def filterLocationName(conn: sqlite3.Connection, locationName: str):
    query = """
    SELECT * FROM MATCH_VIEW
    WHERE location_name == (?);
    """ 
    params = (locationName, )
    res = executeSQL(conn, query, params)
    return res

def filterMatchesWon(conn: sqlite3.Connection, teamName: str):
    query = """
        SELECT * FROM MATCH_VIEW
        WHERE ((team1 = (?) AND score1 >= score2) OR (team2 = (?) AND score2 >= score1)) AND live = false;
        """ 
    params = (teamName, )
    res = executeSQL(conn, query, params)
    return res

def futureNotSoldOut(conn: sqlite3.Connection, date: str):
    query = """
    SELECT v.* FROM MATCH AS m
    JOIN MATCH_VIEW AS v
    ON m.match_id = v.match_id
    JOIN LOCATION AS l
    ON m.location_id = l.location_id
    WHERE (l.seats > m.tickets_sold) AND (m.date > (?)) AND m.live = false
    """ 
    params = (date, )
    res = executeSQL(conn, query, params) 
    return res

def soldOutMatches(conn: sqlite3.Connection, date: str):
    query = """
    SELECT v.* FROM MATCH AS m
    JOIN MATCH_VIEW AS v
    ON m.match_id = v.match_id
    JOIN LOCATION AS l
    ON m.location_id = l.location_id
    WHERE (l.seats = m.tickets_sold) and (m.date > (?))
    """
    params = (date, )
    res = executeSQL(conn, query, params)
    return res

def getLeaderBoard(conn: sqlite3.Connection, sportName: str):
    query = """
    SELECT t.name AS team_name, COUNT(*) AS wins
    FROM TEAM t
    JOIN MATCH m
        ON (t.team_id = m.team1_id AND m.score_team1 >= m.score_team2 AND m.live = false)
        OR (t.team_id = m.team2_id AND m.score_team2 >= m.score_team1 AND m.live = false)
    WHERE t.sport = (?)
    GROUP BY t.team_id
    ORDER BY wins DESC;
    """ 
    params = (sportName, )
    res = executeSQL(conn, query, params)
    return res
