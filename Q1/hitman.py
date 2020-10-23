import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur = conn.cursor()

    HITMAN = """
        SELECT striker, player_name,
        SUM(CASE WHEN runs_scored = 6 THEN 1 ELSE 0 END) AS n_sixes,
        COUNT(ball_id) AS n_balls
        FROM BALL_BY_BALL
        INNER JOIN PLAYER ON BALL_BY_BALL.striker = PLAYER.player_id
        GROUP BY striker
        ORDER BY (n_sixes*1.0/n_balls) DESC, player_name ASC
    """
    # SQLite automatically returns NULL when n_balls will be 0
    cur.execute(HITMAN)
    results = cur.fetchall()

    for r in results:
        print("{},{},{},{},{}".format(r[0], r[1], r[2], r[3], r[2] / r[3]))  # "Hack"

    cur.close()

# Error handling
except sq.Error as error:
    print("Errors: ", error)

# Close the connection
finally:
    if (conn):
        conn.close()
