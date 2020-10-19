import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    PURPLE_CAP = """
        SELECT bowler, player_name, COUNT(out_type) AS n_wickets
        FROM BALL_BY_BALL 
        INNER JOIN PLAYER ON BALL_BY_BALL.bowler = PLAYER.player_id
        WHERE out_type != 'Not Applicable'
        GROUP BY bowler, player_name
        ORDER BY n_wickets DESC
        LIMIT 20;
    """
    cur.execute(PURPLE_CAP)
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