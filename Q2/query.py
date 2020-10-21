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
    cur.executescript("SELECT * FROM {} WHERE {} = '{}'".format(table_name, column_name, query))
    conn.commit()
else:
    cur.execute("SELECT * FROM {} WHERE {} = (?)".format(table_name, column_name), (query,))
    conn.commit()
print(cur.fetchall())

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

if (conn):
    conn.close()
