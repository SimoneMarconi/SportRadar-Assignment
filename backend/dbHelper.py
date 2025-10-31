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
      ON t.team_id IN (m._team1_id, m._team2_id)
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
    ON m._location_id = l.location_id
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
    ON m._location_id = l.location_id
    WHERE (l.seats = m.tickets_sold) and (m.date > (?))
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

def getUpcomingMatches(conn: sqlite3.Connection, sport: Optional[str], date: str):
    res = None
    if sport:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE date > (?) AND sport = (?)
        """ 
        params = (date, sport)
        res = executeSQL(conn, query, params)
    else:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE date > (?)
        """ 
        res = executeSQL(conn, query, None)
    return res

def getFinishedMatches(conn: sqlite3.Connection, sport: Optional[str], date: str):
    res = None
    if sport:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE date < (?) AND sport = (?)
        """ 
        params = (date, sport)
        res = executeSQL(conn, query, params)
    else:
        query = """
        SELECT * FROM MATCH_VIEW
        WHERE date < (?)
        """ 
        res = executeSQL(conn, query, None)
    return res

def getMatch(conn: sqlite3.Connection, match_id: int):
    res = None
    query = """
    SELECT t1.name AS team1, t2.name AS team2, t1.description AS team1_description, t2.description AS team2_description, m.description AS match_description, l.coordinates AS coordinates, m.tickets_sold AS tickets_sold, l.seats AS total_seats
    FROM MATCH as m
    JOIN TEAM AS t1 ON m._team1_id == t1.team_id
    JOIN TEAM AS t2 ON m._team2_id == t2.team_id
    JOIN LOCATION AS l on m._location_id == l.location_id
    WHERE match_id = (?)
    """ 
    params = (match_id, )
    res = executeSQL(conn, query, params)
    return res
