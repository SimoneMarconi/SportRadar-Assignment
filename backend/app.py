from flask import Flask, g, jsonify, request
from flask_cors import CORS
import sqlite3
from dbHelper import *
from validators import *

app = Flask(__name__)
CORS(app)
DATABASE = "sports.db"

def getDb():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

# get all matches in the database
@app.route("/get_all_match", methods=["GET"])
def getAllMatch():
    conn = getDb()
    res = getAll(conn)
    return res
# get all the matches after a specific date
@app.route("/match_after", methods=["POST"])
def getFilteredTime():
    data = request.json
    if not data:
        return jsonify({"message": "missing payload"}), 400
    time = data.get("time")
    if not time:
        return jsonify({"message": "missing time"}), 400
    conn = getDb()
    print(time)
    res = filterAfterTime(conn, time)
    return res

# get the leaderboard data ordered
@app.route("/leaderboard", methods=["GET", "POST"])
def getLeaderboard():
    if request.method == "GET":
        conn = getDb()
        res = getLeaderBoard(conn, None)
        return res
    data = request.json
    if not data:
        return jsonify({"message": "missing payload"}), 400
    sport = data.get("sport")
    if not sport:
        return jsonify({"message": "missing sport"}), 400
    conn = getDb()
    res = getLeaderBoard(conn, sport)
    return res

# get informations for a single match
@app.route("/single_match", methods=["POST"])
def getSingleMatch():
    data = request.json
    if not data:
        return jsonify({"message": "missing payload"}), 400
    id = data.get("match_id")
    if not id:
        return jsonify({"message": "missing id"}), 400
    conn = getDb()
    res = getMatch(conn, id)
    return res

# add a match to the total
@app.route("/add_match", methods=["POST"])
def addMatch():
    data = request.json
    if not data:
        return jsonify({"message": "missing payload"}), 400
    team1 = data.get("team1")
    team2 = data.get("team2")
    location = data.get("location")
    date = data.get("date")
    time = data.get("time")
    description = data.get("description")
    tickets_sold = data.get("tickets_sold")
    conn = getDb()
    if not checkSports(conn, team1, team2):
        return jsonify({"message": "teams play different sports"}), 400
    teamId1 = checkTeam(conn, team1)
    if not teamId1:
        return jsonify({"message": "team1 not found"}), 400
    teamId2 = checkTeam(conn, team2)
    if not teamId2:
        return jsonify({"message": "team2 not found"}), 400
    locationId = checkLocation(conn, location)
    if not locationId:
        return jsonify({"message": "location not found"}), 400
    if not isFutureDate(date):
        return jsonify({"message": "date is not in the future"}), 400
    if insertMatch(conn, teamId1, teamId2, locationId, date, time, description, tickets_sold):
        return jsonify({"message": "match added successfully"}), 200
    else:
        return jsonify({"message": "failed to add match"}), 500
