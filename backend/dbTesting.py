from dbHelper import *
import sqlite3

from validators import checkSports

# testing file to quickly check working of queries and functions

def evaluateQuery():
    connection = sqlite3.connect("sports.db")
    # rows = futureNotSoldOut(cursor, "2025-10-20") 
    # rows = soldOutMatches(cursor)
    # res = getLeaderBoard(connection, "baseball")
    # res = getLiveMatches(connection, None)
    # print(len(json.loads(res)))
    res = checkSports(connection, "Greenfield Giants", "Skyline Shooters")
    # res = checkSports(connection, "Greenfield Giants", "Eagles FC")
    print(res)

if __name__ == "__main__":
    evaluateQuery()
