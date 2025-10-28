import sqlite3

connection = sqlite3.connect("sports.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# LOCATION
cursor.execute("""
CREATE TABLE IF NOT EXISTS LOCATION (
    location_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    seats INT,
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

