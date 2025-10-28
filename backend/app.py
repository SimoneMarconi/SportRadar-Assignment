from flask import Flask, g, jsonify, request
import sqlite3
from dbHelper import *

app = Flask(__name__)
DATABASE = "sports.db"

def getDb():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.route("/get_all_match", methods=["GET"])
def getAllMatch():
    conn = getDb()
    res = getAll(conn)
    return res

@app.route("/match_after", methods=["POST"])
def getFilteredTime():
    data = request.json
    time = None
    if data:
        time = data.get("time")
    if not time:
        return jsonify({"message": "missing time"}), 400
    conn = getDb()
    res = filterAfterTime(conn, time)
    return res

@app.route("/match_team", methods=["POST"])
def getFilterTeam():
    data = request.json
    team = None
    if data:
        team = data.get("team")
    if not team:
        return jsonify({"message": "missing team"}), 400
    conn = getDb()
    res = filterTeamName(conn, team)
    return res

@app.route("/match_sport", methods=["POST"])
def getFilterSport():
    data = request.json
    sport = None
    if data:
        sport = data.get("sport")
    if not sport:
        return jsonify({"message": "missing sport"}), 400
    conn = getDb()
    res = filterTeamName(conn, sport)
    return res

@app.route("/match_location", methods=["POST"])
def getFilterLocation():
    data = request.json
    location = None
    if data:
        location = data.get("location")
    if not location:
        return jsonify({"message": "missing location"}), 400
    conn = getDb()
    res = filterTeamName(conn, location)
    return res


@app.route("/match_won", methods=["POST"])
def getFilterTeamWon():
    data = request.json
    team = None
    if data:
        team = data.get("team")
    if not team:
        return jsonify({"message": "missing team"}), 400
    conn = getDb()
    res = filterTeamName(conn, team)
    return res

@app.route("/match_not_soldout", methods=["POST"])
def getFilterNotSoldOut():
    data = request.json
    date = None
    if data:
        date = data.get("date")
    if not date:
        return jsonify({"message": "missing date"}), 400
    conn = getDb()
    res = futureNotSoldOut(conn, date)
    return res

@app.route("/match_soldout", methods=["POST"])
def getFilterSoldOut():
    data = request.json
    date = None
    if data:
        date = data.get("date")
    if not date:
        return jsonify({"message": "missing date"}), 400
    conn = getDb()
    res = soldOutMatches(conn, date)
    return res

@app.route("/leaderboard", methods=["POST"])
def getLeaderboard():
    data = request.json
    sport = None
    if data:
        sport = data.get("sport")
    if not sport:
        return jsonify({"message": "missing sport"}), 400
    conn = getDb()
    res = getLeaderBoard(conn, sport)
    return res
