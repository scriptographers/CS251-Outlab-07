import csv
import sqlite3 as sq

# CONSTANTS (Hardcoded)
DB_NAME     = "ipl.db"
BASE_PATH   = "" # New PS change mentions this
TABLE_NAMES = ["TEAM", "MATCH", "PLAYER", "PLAYER_MATCH", "BALL_BY_BALL"]
CSV_PATHS   = [(BASE_PATH + tn.lower() + ".csv") for tn in TABLE_NAMES]
N_TABLES    = len(TABLE_NAMES)

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    for i in range(N_TABLES):
        with open(CSV_PATHS[i], 'r') as f:
            rows   = csv.reader(f)
            header = next(rows)
            n_cols = len(header)
            qmarks = ','.join(["?" for _ in range(n_cols)])
            qmarks = "(" + qmarks + ")"
            # Insert into table query
            ITQ = "INSERT INTO {} VALUES {}".format(TABLE_NAMES[i], qmarks)
            cur.executemany(ITQ, rows)
            conn.commit()

    # All tables filled
    cur.close()

# Error handling
except sq.Error as error:
    print("Errors: ", error)

# Close the connection
finally:
    if (conn):
        conn.close()