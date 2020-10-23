import csv
import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    AVG = """
        SELECT venue_name, 
        SUM(runs_scored) AS total_runs,
        COUNT(DISTINCT MATCH.match_id) AS n_matches
        FROM BALL_BY_BALL
        INNER JOIN MATCH ON BALL_BY_BALL.match_id =MATCH.match_id
        GROUP BY venue_name
        ORDER BY (total_runs*1.0/n_matches) DESC
    """
    cur.execute(AVG)
    results = cur.fetchall()

    for r in results:
        if r[2] != 0:
            print("{},{}".format(r[0], r[1]/r[2])) # "Hack"

    cur.close()

# Error handling
except sq.Error as error:
    print("Errors: ", error)

# Close the connection
finally:
    if (conn):
        conn.close()