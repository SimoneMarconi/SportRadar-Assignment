import sqlite3
import datetime

def filterAfterTime(cursor: sqlite3.Cursor, date: datetime.date):
    cursor.execute(
    """
    SELECT * FROM MATCH_VIEW
    WHERE datetime(date) > datetime(?);
    """, ((date, ))
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def filterTeamName(cursor: sqlite3.Cursor, teamName: str):
    cursor.execute(
        """
        SELECT * FROM MATCH_VIEW
        WHERE team1 == (?) OR team2 == (?);
        """, ((teamName, teamName))
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def filterSportName(cursor: sqlite3.Cursor, sportName: str):
    cursor.execute(
        """
        SELECT v.*
        FROM MATCH AS m
        JOIN MATCH_VIEW AS v 
          ON m.match_id = v.match_id
        JOIN TEAM AS t
          ON t.team_id IN (m.team1_id, m.team2_id)
        WHERE t.sport = (?)
        GROUP BY(v.match_id);
        """, (sportName, )
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def filterLocationName(cursor: sqlite3.Cursor, locationName: str):
    cursor.execute(
        """
        SELECT * FROM MATCH_VIEW
        WHERE location_name == (?);
        """, ((locationName, ))
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def filterMatchesWon(cursor: sqlite3.Cursor, teamName: str):
    cursor.execute(
        """
        SELECT * FROM MATCH_VIEW
        WHERE (team1 = (?) AND score1 >= score2) OR (team2 = (?) AND score2 >= score1);
        """, ((teamName, ))
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def futureNotSoldOut(cursor: sqlite3.Cursor, date: str):
    cursor.execute(
        """
        SELECT v.* FROM MATCH AS m
        JOIN MATCH_VIEW AS v
        ON m.match_id = v.match_id
        JOIN LOCATION AS l
        ON m.location_id = l.location_id
        WHERE (l.seats > m.tickets_sold) and (m.date > (?))
        """, ((date, ))
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def soldOutMatches(cursor: sqlite3.Cursor):
    cursor.execute(
        """
        SELECT v.* FROM MATCH AS m
        JOIN MATCH_VIEW AS v
        ON m.match_id = v.match_id
        JOIN LOCATION AS l
        ON m.location_id = l.location_id
        WHERE (l.seats = m.tickets_sold)
        """
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def getLeaderBoard(cursor: sqlite3.Cursor, sportName: str):

    cursor.execute("""
    SELECT t.name AS team_name, COUNT(*) AS wins
    FROM TEAM t
    JOIN MATCH m
        ON (t.team_id = m.team1_id AND m.score_team1 >= m.score_team2)
        OR (t.team_id = m.team2_id AND m.score_team2 >= m.score_team1)
    WHERE t.sport = (?)
    GROUP BY t.team_id
    ORDER BY wins DESC;
    """, (sportName, ))
    rows = cursor.fetchall()
    cursor.close()
    return rows
