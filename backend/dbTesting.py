from dbHelper import *
import sqlite3

def evaluateQuery():
    connection = sqlite3.connect("sports.db")
    # rows = futureNotSoldOut(cursor, "2025-10-20") 
    # rows = soldOutMatches(cursor)
    rows = getLeaderBoard(connection, "baseball")
    for r in rows:
        print(r)

if __name__ == "__main__":
    evaluateQuery()
