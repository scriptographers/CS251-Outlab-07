import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    DELETE = "DROP TABLE IF EXISTS POINTS_TABLE;"
    cur.execute(DELETE)
    conn.commit()

    CREATE = """
        CREATE TABLE IF NOT EXISTS POINTS_TABLE 
        (
            team_id INTEGER PRIMARY KEY, 
            team_name TEXT,
            points INTEGER DEFAULT 0,
            nrr DECIMAL DEFAULT 0
        );
    """
    cur.execute(CREATE)
    conn.commit()

    GET_TEAMS = "SELECT team_id, team_name FROM TEAM"
    cur.execute(GET_TEAMS)
    teams = cur.fetchall()

    TEAM_POINTS = {team[0]:0 for team in teams}
    TEAM_NRR = {team[0]:0 for team in teams}

    GET_DATA = "SELECT * FROM MATCH"
    cur.execute(GET_DATA)
    rows = cur.fetchall()

    for row in rows:

        team1 = int(row[2])
        team2 = int(row[3])
        winner = row[9]
        margin = row[-1]
        win_type = row[12]

        if win_type.lower() != "tie":
            if winner != "NULL":
                winner = int(winner)
                TEAM_POINTS[winner] += 2
            else:
                # Match abandoned
                TEAM_POINTS[team1] += 1
                TEAM_POINTS[team2] += 1
        else:
            TEAM_POINTS[team1] += 1
            TEAM_POINTS[team2] += 1

        nrr = 0
        if margin != "NULL":
            margin = int(margin)
            if win_type == "runs":
                nrr = margin/20
            elif win_type == "wickets":
                nrr = margin/10
            else:
                nrr = 0

        # NRR changes only when there is a winner
        if team1 == winner:
            TEAM_NRR[team1] += nrr
            TEAM_NRR[team2] -= nrr
        elif team2 == winner:
            TEAM_NRR[team1] -= nrr
            TEAM_NRR[team2] += nrr

    DATA = []
    for team in teams: 
        DATA.append((team[0], team[1], TEAM_POINTS[team[0]], TEAM_NRR[team[0]]))
    DATA = sorted(DATA, key=lambda val: (val[2], val[3]), reverse=True)

    ADD_DATA = "INSERT INTO POINTS_TABLE (team_id, team_name, points, nrr) VALUES (?, ?, ?, ?)"
    cur.executemany(ADD_DATA, DATA)
    conn.commit()

    for i in range(len(DATA)):
        print("{},{},{},{}".format(i+1, DATA[i][1], DATA[i][2], DATA[i][3]))

    cur.close()

# Error handling
except sq.Error as error:
    print("Errors: ", error)

# Close the connection
finally:
    if (conn):
        conn.close()