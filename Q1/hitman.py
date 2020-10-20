import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur = conn.cursor()

    SMQ = """
        SELECT striker, player_name, COUNT(*) AS total,
        COUNT(CASE WHEN runs_scored=6 THEN 1 END) AS sixes,
        COUNT(CASE WHEN runs_scored=6 THEN 1 END)*1.0/COUNT(*) AS avg
        FROM BALL_BY_BALL
        INNER JOIN PLAYER ON BALL_BY_BALL.striker = PLAYER.player_id
        GROUP BY player_name
        ORDER BY avg DESC
   """

    cur.execute(SMQ)
    results = cur.fetchall()

    # print(results)
    for r in results:
        print("{},{},{},{},{}".format(r[0], r[1], r[2], r[3], r[4]))

    cur.close()


# Error handling
except sq.Error as error:
    print("Errors: ", error)


# Close the connection
finally:
    if (conn):
        conn.close()
