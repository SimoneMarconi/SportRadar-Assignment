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
    ("2025-01-12", "18:00", 1, 2, 1, "3:2", "Season opener between two classic rivals.", 65000),
    ("2025-02-08", "20:30", 3, 4, 4, "1:1", None, 38000),
    ("2025-03-15", "17:00", 1, 11, 3, "2:0", None, 11000),
    ("2025-04-02", "21:00", 13, 2, 6, "4:3", "Thrilling European derby.", 23000),
    ("2025-05-10", "19:00", 4, 11, 4, "0:1", None, 30000),
    ("2025-06-22", "18:30", 1, 13, 10, "2:2", None, 27000),
    ("2025-09-05", "18:00", 1, 3, 1, None, "Preseason friendly match.", 50000),
    ("2025-09-12", "20:00", 2, 11, 4, None, None, 35000),
    ("2025-09-20", "19:30", 4, 13, 6, None, None, 20000),

    # Basketball
    ("2025-01-20", "19:30", 5, 6, 5, "89:84", "Opening basketball night.", 16000),
    ("2025-02-12", "18:00", 7, 12, 2, "76:88", None, 14000),
    ("2025-03-10", "20:00", 6, 15, 7, "101:99", "A close and intense game.", 21000),
    ("2025-04-05", "19:45", 15, 5, 7, "95:87", None, 20000),
    ("2025-05-14", "18:30", 12, 7, 2, "90:92", None, 12000),
    ("2025-06-01", "20:15", 15, 6, 7, "88:91", None, 21000),
    ("2025-09-25", "18:45", 5, 15, 5, None, "exhibition match.", 14000),
    ("2025-10-02", "20:15", 6, 12, 2, None, None, 15000),
    ("2025-10-10", "19:00", 7, 15, 7, None, None, 18000),

    # Baseball
    ("2025-01-25", "15:00", 8, 9, 6, "7:5", "Opening baseball weekend.", 20000),
    ("2025-02-28", "16:00", 10, 14, 8, "3:4", None, 32000),
    ("2025-03-22", "14:00", 8, 10, 9, "2:1", None, 16000),
    ("2025-04-17", "17:30", 9, 14, 8, "5:6", None, 34000),
    ("2025-05-20", "15:45", 14, 8, 8, "8:9", None, 33000),
    ("2025-06-30", "16:15", 10, 9, 9, "4:4", "Friendly preseason match.", 15000),
    ("2025-10-15", "16:00", 8, 14, 8, None, None, 31000),
    ("2025-10-22", "15:30", 9, 10, 9, None, None, 15000),
    ("2025-10-30", "17:00", 14, 8, 8, None, "Upcoming league match.", 32000),
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
    team1_id INTEGER NOT NULL,
    team2_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    score TEXT,
    description TEXT,
    tickets_sold INT,
    FOREIGN KEY (team1_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (team2_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (location_id) REFERENCES LOCATION(location_id)
);
""")

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
    score TEXT,
    description TEXT,
    tickets_sold INT,
    FOREIGN KEY (team1_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (team2_id) REFERENCES TEAM(team_id),
    FOREIGN KEY (location_id) REFERENCES LOCATION(location_id)
);
""")

cursor.executemany("""
INSERT INTO LOCATION (name, seats, coordinates) VALUES (?, ?, ?)
""", locations)

cursor.executemany("""
INSERT INTO TEAM (name, sport, location_id, description) VALUES (?, ?, ?, ?)
""", teams)

cursor.executemany("""
INSERT INTO MATCH (date, time, team1_id, team2_id, location_id, score, description, tickets_sold) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", matches)

connection.commit()
connection.close()
