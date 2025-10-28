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
    ("2025-01-12", "18:00", 1, 2, 1, "Season opener between two classic rivals.", 65000),
    ("2025-02-08", "20:30", 3, 4, 4, None, 38000),
    ("2025-03-15", "17:00", 1, 11, 3, None, 11000),
    ("2025-04-02", "21:00", 13, 2, 6, "Thrilling European derby.", 23000),
    ("2025-05-10", "19:00", 4, 11, 4, None, 30000),
    ("2025-06-22", "18:30", 1, 13, 10, None, 27000),
    ("2025-09-05", "18:00", 1, 3, 1, "Preseason friendly match.", 50000),
    ("2025-09-12", "20:00", 2, 11, 4, None, 35000),
    ("2025-09-20", "19:30", 4, 13, 6, None, 20000),

    # Basketball
    ("2025-01-20", "19:30", 5, 6, 5, "Opening basketball night.", 16000),
    ("2025-02-12", "18:00", 7, 12, 2, None, 14000),
    ("2025-03-10", "20:00", 6, 15, 7, "A close and intense game.", 21000),
    ("2025-04-05", "19:45", 15, 5, 7, None, 20000),
    ("2025-05-14", "18:30", 12, 7, 2, None, 12000),
    ("2025-06-01", "20:15", 15, 6, 7, None, 21000),
    ("2025-09-25", "18:45", 5, 15, 5, "exhibition match.", 14000),
    ("2025-10-02", "20:15", 6, 12, 2, None, 15000),
    ("2025-10-10", "19:00", 7, 15, 7, None, 18000),

    # Baseball
    ("2025-01-25", "15:00", 8, 9, 6, "Opening baseball weekend.", 20000),
    ("2025-02-28", "16:00", 10, 14, 8, None, 32000),
    ("2025-03-22", "14:00", 8, 10, 9, None, 16000),
    ("2025-04-17", "17:30", 9, 14, 8, None, 34000),
    ("2025-05-20", "15:45", 14, 8, 8, None, 33000),
    ("2025-06-30", "16:15", 10, 9, 9, "Friendly preseason match.", 15000),
    ("2025-10-15", "16:00", 8, 14, 8, None, 31000),
    ("2025-10-22", "15:30", 9, 10, 9, None, 15000),
    ("2025-10-30", "17:00", 14, 8, 8, "Upcoming league match.", 32000),
]

scores = [
    # Match 1: Team 1 vs Team 2, Winner: 1
    (1, 1, 2, 1),
    (1, 2, 1, 0),
    
    # Match 2: Team 3 vs Team 4, Winner: 4
    (2, 3, 1, 0),
    (2, 4, 2, 1),
    
    # Match 3: Team 1 vs Team 11, Winner: 3 (draw)
    (3, 1, 1, 0),
    (3, 11, 1, 0),
    
    # Match 4: Team 13 vs Team 2, Winner: 6 (draw)
    (4, 13, 2, 0),
    (4, 2, 2, 0),
    
    # Match 5: Team 4 vs Team 11, Winner: 4
    (5, 4, 3, 1),
    (5, 11, 1, 0),
    
    # Match 6: Team 1 vs Team 13, Winner: 10 (draw)
    (6, 1, 2, 0),
    (6, 13, 2, 0),
    
    # Match 7: Team 1 vs Team 3, Winner: 1
    (7, 1, 3, 1),
    (7, 3, 2, 0),
    
    # Match 8: Team 2 vs Team 11, Winner: 4 (draw)
    (8, 2, 1, 0),
    (8, 11, 1, 0),
    
    # Match 9: Team 4 vs Team 13, Winner: 6 (draw)
    (9, 4, 1, 0),
    (9, 13, 1, 0),
    
    # Match 10: Team 5 vs Team 6, Winner: 5
    (10, 5, 3, 1),
    (10, 6, 2, 0),
    
    # Match 11: Team 7 vs Team 12, Winner: 2 (draw)
    (11, 7, 1, 0),
    (11, 12, 1, 0),
    
    # Match 12: Team 6 vs Team 15, Winner: 7 (draw)
    (12, 6, 2, 0),
    (12, 15, 2, 0),
    
    # Match 13: Team 15 vs Team 5, Winner: 7 (draw)
    (13, 15, 2, 0),
    (13, 5, 2, 0),
    
    # Match 14: Team 12 vs Team 7, Winner: 2 (draw)
    (14, 12, 1, 0),
    (14, 7, 1, 0),
    
    # Match 15: Team 15 vs Team 6, Winner: 7 (draw)
    (15, 15, 2, 0),
    (15, 6, 2, 0),
    
    # Match 16: Team 5 vs Team 15, Winner: 5
    (16, 5, 3, 1),
    (16, 15, 2, 0),
    
    # Match 17: Team 6 vs Team 12, Winner: 2 (draw)
    (17, 6, 1, 0),
    (17, 12, 1, 0),
    
    # Match 18: Team 7 vs Team 15, Winner: 7
    (18, 7, 3, 1),
    (18, 15, 2, 0),
    
    # Match 19: Team 8 vs Team 9, Winner: 6 (draw)
    (19, 8, 2, 0),
    (19, 9, 2, 0),
    
    # Match 20: Team 10 vs Team 14, Winner: 8 (draw)
    (20, 10, 3, 0),
    (20, 14, 3, 0),
    
    # Match 21: Team 8 vs Team 10, Winner: 9 (draw)
    (21, 8, 2, 0),
    (21, 10, 2, 0),
    
    # Match 22: Team 9 vs Team 14, Winner: 8 (draw)
    (22, 9, 3, 0),
    (22, 14, 3, 0),
    
    # Match 23: Team 14 vs Team 8, Winner: 8
    (23, 14, 2, 0),
    (23, 8, 4, 1),
    
    # Match 24: Team 10 vs Team 9, Winner: 9
    (24, 10, 1, 0),
    (24, 9, 3, 1),
    
    # Match 25: Team 8 vs Team 14, Winner: 8
    (25, 8, 5, 1),
    (25, 14, 3, 0),
    
    # Match 26: Team 9 vs Team 10, Winner: 9
    (26, 9, 4, 1),
    (26, 10, 2, 0),
    
    # Match 27: Team 14 vs Team 8, Winner: 8
    (27, 14, 2, 0),
    (27, 8, 5, 1),
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
    location_id INTEGER,
    description TEXT,
    tickets_sold INT,
    FOREIGN KEY (team1_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (team2_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (location_id) REFERENCES LOCATION(location_id)
    CHECK(team1_id <> team2_id)
);
""")

# SCORE
cursor.execute("""
CREATE TABLE IF NOT EXISTS SCORE(
    match_id INTEGER,
    team_id INTEGER,
    scored INTEGER NOT NULL,
    points INTEGER NOT NULL,
    PRIMARY KEY(match_id, team_id),
    FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
    FOREIGN KEY(team_id) REFERENCES TEAM(team_id)
);
""")

cursor.executemany("""
INSERT INTO LOCATION (name, seats, coordinates) VALUES (?, ?, ?)
""", locations)

cursor.executemany("""
INSERT INTO TEAM (name, sport, location_id, description) VALUES (?, ?, ?, ?)
""", teams)

cursor.executemany("""
INSERT INTO MATCH (date, time, team1_id, team2_id, location_id, description, tickets_sold) VALUES (?, ?, ?, ?, ?, ?, ?)
""", matches)

cursor.executemany("""
INSERT INTO SCORE(match_id, team_id, scored, points) VALUES (?, ?, ?, ?)
""", scores)

connection.commit()
connection.close()
