from dbHelper import *
import sqlite3

def evaluateQuery():
    connection = sqlite3.connect("sports.db")
    # rows = futureNotSoldOut(cursor, "2025-10-20") 
    # rows = soldOutMatches(cursor)
    # res = getLeaderBoard(connection, "baseball")
    res = getLiveMatches(connection, None)
    print(len(json.loads(res)))
    print(res)

if __name__ == "__main__":
    evaluateQuery()
