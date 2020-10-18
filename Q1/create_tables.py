import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    # (a) Query for creating the TEAM table
    CTQ = """
    CREATE TABLE IF NOT EXISTS TEAM 
    (
        team_id INTEGER PRIMARY KEY,
        team_name TEXT
    );
    """
    cur.execute(CTQ)
    conn.commit()


    # (b) Query for creating the PLAYER table
    CPQ = """
    CREATE TABLE IF NOT EXISTS PLAYER 
    (
        player_id INTEGER PRIMARY KEY,
        player_name TEXT,
        dob TIMESTAMP,
        batting_hand TEXT,
        bowling_skill TEXT,
        country_name TEXT
    );
    """
    cur.execute(CPQ)
    conn.commit()


    # (c) Query for creating the MATCH table
    CMQ = """
    CREATE TABLE IF NOT EXISTS MATCH 
    (
        match_id INTEGER PRIMARY KEY,
        season_year INTEGER,
        team1 INTEGER,
        team2 INTEGER,
        battedfirst INTEGER,
        battedsecond INTEGER,
        venue_name TEXT,
        city_name TEXT,
        country_name TEXT,
        toss_winner TEXT,
        match_winner TEXT,
        toss_name TEXT,
        win_type TEXT,
        man_of_match INTEGER,
        win_margin INTEGER,

        FOREIGN KEY (team1) REFERENCES TEAM(team_id),
        FOREIGN KEY (team2) REFERENCES TEAM(team_id),
        FOREIGN KEY (battedfirst) REFERENCES TEAM(team_id),
        FOREIGN KEY (battedsecond) REFERENCES TEAM(team_id)
    );
    """
    cur.execute(CMQ)
    conn.commit()


    # (d) Query for creating the PLAYER_MATCH table
    CPMQ = """
    CREATE TABLE IF NOT EXISTS PLAYER_MATCH 
    (
        playermatch_key BIGINT PRIMARY KEY,
        match_id INTEGER,
        player_id INTEGER,
        batting_hand TEXT,
        bowling_skill TEXT,
        role_desc TEXT,
        team_id INTEGER,

        FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
        FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
        FOREIGN KEY (team_id) REFERENCES TEAM(team_id)
    );
    """
    cur.execute(CPMQ)
    conn.commit()


    # (e) Query for creating the BALL_BY_BALL table
    CBBQ = """
    CREATE TABLE IF NOT EXISTS BALL_BY_BALL 
    (
        match_id INTEGER,
        innings_no INTEGER,
        over_id INTEGER,
        ball_id INTEGER,
        striker_batting_position INTEGER,
        runs_scored INTEGER,
        extra_runs INTEGER,
        out_type TEXT,
        striker INTEGER,
        non_striker INTEGER,
        bowler INTEGER,

        FOREIGN KEY (match_id) REFERENCES MATCH(match_id),
        FOREIGN KEY (striker) REFERENCES PLAYER(player_id),
        FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id),
        FOREIGN KEY (bowler) REFERENCES PLAYER(player_id),

        PRIMARY KEY (match_id, innings_no, over_id, ball_id)
    );
    """
    cur.execute(CBBQ)
    conn.commit()

    # All tables created
    cur.close()

# Error handling
except sq.Error as error:
    print("Errors: ", error)

# Close the connection
finally:
    if (conn):
        conn.close()


# DOUBTS: NOT NULL? AUTOINCREMENT?