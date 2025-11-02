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

@app.route("/get_all_match", methods=["GET"])
def getAllMatch():
    conn = getDb()
    res = getAll(conn)
    return res

# @app.route("/match_after", methods=["POST"])
# def getFilteredTime():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     time = data.get("time")
#     if not time:
#         return jsonify({"message": "missing time"}), 400
#     conn = getDb()
#     res = filterAfterTime(conn, time)
#     return res
#
# @app.route("/match_team", methods=["POST"])
# def getFilterTeam():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     team = data.get("team")
#     if not team:
#         return jsonify({"message": "missing team"}), 400
#     conn = getDb()
#     res = filterTeamName(conn, team)
#     return res
#
# @app.route("/match_sport", methods=["POST"])
# def getFilterSport():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     sport = data.get("sport")
#     if not sport:
#         return jsonify({"message": "missing sport"}), 400
#     conn = getDb()
#     res = filterTeamName(conn, sport)
#     return res
#
# @app.route("/match_location", methods=["POST"])
# def getFilterLocation():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     location = data.get("location")
#     if not location:
#         return jsonify({"message": "missing location"}), 400
#     conn = getDb()
#     res = filterTeamName(conn, location)
#     return res
#
#
# @app.route("/match_won", methods=["POST"])
# def getFilterTeamWon():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     team = data.get("team")
#     if not team:
#         return jsonify({"message": "missing team"}), 400
#     conn = getDb()
#     res = filterTeamName(conn, team)
#     return res
#
# @app.route("/match_not_soldout", methods=["POST"])
# def getFilterNotSoldOut():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     date = data.get("date")
#     if not date:
#         return jsonify({"message": "missing date"}), 400
#     conn = getDb()
#     res = futureNotSoldOut(conn, date)
#     return res
#
# @app.route("/match_soldout", methods=["POST"])
# def getFilterSoldOut():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     date = data.get("date")
#     if not date:
#         return jsonify({"message": "missing date"}), 400
#     conn = getDb()
#     res = soldOutMatches(conn, date)
#     return res

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


# @app.route("/live_matches", methods=["POST"])
# def getLive():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     sport = data.get("sport")
#     if sport:
#         conn = getDb()
#         res = getLiveMatches(conn, sport)
#     else:
#         conn = getDb()
#         res = getLiveMatches(conn, None)
#     return res

# @app.route("/upcoming_matches", methods=["POST"])
# def getUpcoming():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     sport = data.get("sport")
#     date = data.get("date")
#     if not date:
#         return jsonify({"message": "missing date"}), 400
#     if sport:
#         conn = getDb()
#         res = getUpcomingMatches(conn, sport, date)
#     else:
#         conn = getDb()
#         res = getUpcomingMatches(conn, None, date)
#     return res

# @app.route("/finished_matches", methods=["POST"])
# def getFinished():
#     data = request.json
#     if not data:
#         return jsonify({"message": "missing payload"}), 400
#     sport = data.get("sport")
#     date = data.get("date")
#     if not date:
#         return jsonify({"message": "missing date"}), 400
#     if sport:
#         conn = getDb()
#         res = getFinishedMatches(conn, sport, date)
#     else:
#         conn = getDb()
#         res = getFinishedMatches(conn, None, date)
#     return res

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
