import csv
import sqlite3 as sq

DB_NAME = "ipl.db"

try:
    conn = sq.connect(DB_NAME)
    cur  = conn.cursor()

    SMQ = "SELECT match_id, venue_name FROM MATCH WHERE venue_name is NOT NULL"

    cur.execute(SMQ)
    results = cur.fetchall()

    VENUE_RUNS = { venue:0 for _, venue in results }
    VENUE_N_MATCHES = { venue:0 for _, venue in results }

    for m_id, venue in results:

        SBBQ = "SELECT SUM(runs_scored) FROM BALL_BY_BALL WHERE match_id=?"
        cur.execute(SBBQ, (m_id,))
        total_runs_scored = cur.fetchall()[0][0]

        if (total_runs_scored != None):
            VENUE_N_MATCHES[venue] += 1
            VENUE_RUNS[venue] += total_runs_scored
        # else:
        #    print(m_id)

    VENUE_AVG = { 
        venue: (VENUE_RUNS[venue]/VENUE_N_MATCHES[venue])
        for _,venue in results if (VENUE_N_MATCHES[venue] != 0) 
    }

    VENUE_AVG = { 
        venue: avg 
        for venue,avg in sorted(VENUE_AVG.items(), key=lambda item:item[1], reverse=True) 
    }

    for venue, avg in VENUE_AVG.items():
        print("{},{}".format(venue, avg))
    
    cur.close()


# Error handling
except sq.Error as error:
    print("Errors: ", error)


# Close the connection
finally:
    if (conn):
        conn.close()