import sqlite3

connection = sqlite3.connect("sports.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

locations = [
    ("Olympic Stadium", 70000, "41.8902, 12.4924"),
    ("Downtown Arena", 15000, "40.7128, -74.0060"),
    ("Riverside Park", 12000, "34.0522, -118.2437"),
    ("Greenfield Stadium", 40000, "51.5074, -0.1278"),
    ("Sunset Dome", 18000, "37.7749, -122.4194"),
    ("Central Field", 25000, "48.8566, 2.3522"),
    ("Skyline Arena", 22000, "52.5200, 13.4050"),
    ("Seaside Stadium", 35000, "36.1699, -115.1398"),
    ("Hilltop Field", 17000, "45.4642, 9.1900"),
    ("Grand Park", 28000, "41.9028, 12.4964")
]

teams = [
    ("Eagles FC", "football", 1, "A top-tier football club known for its aggressive play and loyal fan base."),
    ("Lions United", "football", 4, "A historic football team with multiple championship titles."),
    ("Riverside Rangers", "football", 3, "A mid-level football team famous for nurturing young talent."),
    ("Greenfield Giants", "football", 4, "Well-structured defense and long-time rivalry with Lions United."),
    ("Sunset Hoopers", "basketball", 5, "Dynamic basketball team known for their fast breaks."),
    ("Downtown Dribblers", "basketball", 2, "One of the most popular basketball teams in the region."),
    ("Skyline Shooters", "basketball", 7, "Young basketball team focused on precision and teamwork."),
    ("Central Sluggers", "baseball", 6, "A baseball team with a long tradition of powerful hitters."),
    ("Seaside Mariners", "baseball", 8, "Known for their strong pitching rotation."),
    ("Hilltop Hawks", "baseball", 9, "A promising baseball club with a growing fan base."),
    ("Urban Kickers", "football", None, "Nomadic football team often playing away games."),
    ("Downtown Dunkers", "basketball", 2, "A passionate basketball team focusing on defensive play."),
    ("Paris Panthers", "football", 6, "A European club with an international following."),
    ("Vegas Vipers", "baseball", 8, "A new but ambitious baseball franchise."),
    ("Berlin Ballers", "basketball", None, "An emerging team with no fixed home yet, focused on outreach tournaments.")
]

matches = [
    # Football
    ("2025-01-12", "18:00", 1, 2, 1, "Season opener between two classic rivals.", 65000, 2, 1, False),
    ("2025-02-08", "20:30", 3, 4, 4, None, 38000, 1, 2, False),
    ("2025-03-15", "17:00", 1, 11, 3, None, 11000, 1, 1, False),
    ("2025-04-02", "21:00", 13, 2, 6, "Thrilling European derby.", 23000, 2, 2, False),
    ("2025-05-10", "19:00", 4, 11, 4, None, 30000, 3, 1, False),
    ("2025-06-22", "18:30", 1, 13, 10, None, 27000, 2, 2, False),
    ("2025-09-05", "18:00", 1, 3, 1, "Preseason friendly match.", 50000, 3, 2, False),
    ("2025-09-12", "20:00", 2, 11, 4, None, 35000, 1, 1, False),
    ("2025-09-20", "19:30", 4, 13, 6, None, 20000, 1, 1, False),
    ("2025-10-20", "19:30", 4, 13, 6, None, 20000, 0, 0, True),
    ("2025-10-20", "18:30", 1, 2, 1, None, 20000, 1, 0, True),

    # Basketball
    ("2025-01-20", "19:30", 5, 6, 5, "Opening basketball night.", 16000, 3, 2, False),
    ("2025-02-12", "18:00", 7, 12, 2, None, 14000, 1, 1, False),
    ("2025-03-10", "20:00", 6, 15, 7, "A close and intense game.", 21000, 2, 2, False),
    ("2025-04-05", "19:45", 15, 5, 7, None, 20000, 2, 2, False),
    ("2025-05-14", "18:30", 12, 7, 2, None, 12000, 1, 1, False),
    ("2025-06-01", "20:15", 15, 6, 7, None, 21000, 2, 2, False),
    ("2025-09-25", "18:45", 5, 15, 5, "exhibition match.", 14000, 3, 2, False),
    ("2025-10-02", "20:15", 6, 12, 2, None, 15000, 1, 1, False),
    ("2025-10-20", "19:00", 7, 15, 7, None, 18000, 3, 2, True),

    # Baseball
    ("2025-01-25", "15:00", 8, 9, 6, "Opening baseball weekend.", 20000, 2, 2, False),
    ("2025-02-28", "16:00", 10, 14, 8, None, 32000, 3, 3, False),
    ("2025-03-22", "14:00", 8, 10, 9, None, 16000, 2, 2, False),
    ("2025-04-17", "17:30", 9, 14, 8, None, 34000, 3, 3, False),
    ("2025-05-20", "15:45", 14, 8, 8, None, 33000, 2, 4, False),
    ("2025-06-30", "16:15", 10, 9, 9, "Friendly preseason match.", 15000, 1, 3, False),
    ("2025-10-15", "16:00", 8, 14, 8, None, 31000, 5, 3, False),
    ("2025-10-30", "17:00", 14, 8, 8, "Upcoming league match.", 32000, 2, 5, False),
    ("2025-10-20", "19:30", 9, 10, 9, None, 15000, 4, 2, True),
]


# LOCATION
cursor.execute("""
CREATE TABLE IF NOT EXISTS LOCATION (
    location_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    seats INT NOT NULL,
    coordinates TEXT
);
""")

# TEAM
cursor.execute("""
CREATE TABLE IF NOT EXISTS TEAM (
    team_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sport TEXT NOT NULL,
    location_id INTEGER,
    description TEXT,
    FOREIGN KEY (location_id) REFERENCES LOCATION(location_id)
);
""")

# MATCH
cursor.execute("""
CREATE TABLE IF NOT EXISTS MATCH (
    match_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    team1_id INTEGER,
    team2_id INTEGER,
    score_team1 INTEGER,
    score_team2 INTEGER,
    location_id INTEGER,
    description TEXT,
    tickets_sold INT,
    live BOOLEAN,
    FOREIGN KEY (team1_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (team2_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (location_id) REFERENCES LOCATION(location_id)
    CHECK(team1_id <> team2_id)
);
""")

# SCORE
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS SCORE(
#     match_id INTEGER,
#     team_id INTEGER,
#     scored INTEGER NOT NULL,
#     points INTEGER NOT NULL,
#     PRIMARY KEY(match_id, team_id),
#     FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
#     FOREIGN KEY(team_id) REFERENCES TEAM(team_id)
# );
# """)

# MATCHES VIEW
# cursor.execute("""
#     CREATE VIEW IF NOT EXISTS MATCH_VIEW AS
#     SELECT m.match_id,
#     m.date,
#     m.time,
#     t1.name AS team1,
#     t2.name AS team2,
#     s1.scored AS team1_score,
#     s2.scored AS team2_score,
#     m.location_id,
#     m.description,
#     m.tickets_sold
#     FROM TEAM t
#     JOIN MATCH m ON (t.team_id = m.team1_id OR t.team_id = m.team2_id)
#     JOIN TEAM t1 ON m.team1_id = t1.team_id
#     JOIN TEAM t2 ON m.team2_id = t2.team_id
#     LEFT JOIN SCORE s1 ON m.match_id = s1.match_id AND s1.team_id = m.team1_id
#     LEFT JOIN SCORE s2 ON m.match_id = s2.match_id AND s2.team_id = m.team2_id
#     GROUP BY(m.match_id)
# """)

# MATCHES VIEW
cursor.execute(
    """
    CREATE VIEW IF NOT EXISTS MATCH_VIEW AS
    SELECT m.match_id AS match_id, m.date AS date, m.time AS time, t1.name AS team1, t2.name AS team2, m.score_team1 AS score1, m.score_team2 AS score2, l.name AS location_name, m.description AS description, m.tickets_sold AS tickets_sold, m.live AS live
    FROM MATCH as m
    JOIN TEAM AS t1 ON m.team1_id == t1.team_id
    JOIN TEAM AS t2 ON m.team2_id == t2.team_id
    JOIN LOCATION AS l on m.location_id == l.location_id
    """
)

cursor.executemany("""
INSERT INTO LOCATION (name, seats, coordinates) VALUES (?, ?, ?)
""", locations)

cursor.executemany("""
INSERT INTO TEAM (name, sport, location_id, description) VALUES (?, ?, ?, ?)
""", teams)

cursor.executemany("""
INSERT INTO MATCH (date, time, team1_id, team2_id, location_id, description, tickets_sold, score_team1, score_team2, live) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", matches)

# cursor.executemany("""
# INSERT INTO SCORE(match_id, team_id, scored, points) VALUES (?, ?, ?, ?)
# """, scores)

connection.commit()
connection.close()
