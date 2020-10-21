import sys
import sqlite3 as sql

op = sys.argv[1]

DB_NAME = "ipl.db"

conn = sql.connect(DB_NAME)
cur = conn.cursor()

if op == "1":  # TEAM
    ADD_DATA = "INSERT INTO TEAM (team_id, team_name) VALUES (?, ?)"
    cur.execute(ADD_DATA, sys.argv[2:4])
elif op == "2":  # PLAYER
    ADD_DATA = "INSERT INTO PLAYER (player_id, player_name, dob, batting_hand, bowling_skill, country_name) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(ADD_DATA, sys.argv[2:8])
elif op == "3":  # MATCH
    ADD_DATA = "INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(ADD_DATA, sys.argv[2:17])
elif op == "4":  # PLAYER_MATCH
    ADD_DATA = "INSERT INTO PLAYER_MATCH (playermatch_key, match_id, player_id, batting_hand, bowling_skill, role_desc, team_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cur.execute(ADD_DATA, sys.argv[2:9])
else:  # BALL_BY_BALL
    ADD_DATA = "INSERT INTO BALL_BY_BALL (match_id, innings_no, over_id, ball_id, striker_batting_position, runs_scored, extra_runs, out_type, striker, non_striker, bowler) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(ADD_DATA, sys.argv[2:13])

conn.commit()


# xx = ['prereq',
#       'time_slot',
#       'advisor',
#       'takes',
#       'student',
#       'teaches',
#       'section',
#       'instructor',
#       'course',
#       'department',
#       'classroom']
# for i in xx:
#     cur.execute("SELECT COUNT(*) FROM {}".format(i))
#     print(i, cur.fetchall()[0][0])
CHECK = "SELECT * FROM TEAM"
cur.execute(CHECK)
print(cur.fetchall())

if (conn):
    conn.close()
