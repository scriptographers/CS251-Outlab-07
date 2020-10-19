import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    ORANGE_CAP = """
        SELECT striker, player_name, SUM(runs_scored) as total_runs
        FROM BALL_BY_BALL
        INNER JOIN PLAYER ON BALL_BY_BALL.striker = PLAYER.player_id
        GROUP BY striker, player_name
        ORDER BY total_runs DESC
        LIMIT 20;
    """

    cur.execute(ORANGE_CAP)
    results = cur.fetchall()

    for r in results:
        print("{},{},{}".format(r[0], r[1], r[2]))

    cur.close()


# Error handling
except sq.Error as error:
    print("Errors: ", error)


# Close the connection
finally:
    if (conn):
        conn.close()