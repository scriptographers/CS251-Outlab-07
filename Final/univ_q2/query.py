import sys
import sqlite3 as sql

op = sys.argv[1]
table_name = sys.argv[2]
column_name = sys.argv[3]
query = sys.argv[4]

DB_NAME = "univ.db"

conn = sql.connect(DB_NAME)
cur = conn.cursor()

if (op == "0"):
    cur.execute("SELECT * FROM {} WHERE {} = '".format(table_name, column_name) + query + "'")
    conn.commit()
else:
    cur.execute("SELECT * FROM {} WHERE {} = (?)".format(table_name, column_name), (query,))
    conn.commit()
res = cur.fetchall()
for row in res:
    print(','.join(str(x) for x in row))

cur.close()

if (conn):
    conn.close()
