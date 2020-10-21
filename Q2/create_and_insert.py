import sqlite3 as sql

crt = open('University Schema', 'r').read()
ins = open('smallRelationsInsertFile.sql', 'r').read()
DB_NAME = "univ.db"

conn = sql.connect(DB_NAME)
cur = conn.cursor()

for x in crt.split(';') + ins.split(';'):
    try:
        cur.execute(x)
        conn.commit()
    except sql.Error as error:
        continue

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
#     cur.execute("SELECT * FROM {}".format(i))
#     print(cur.fetchall())

if (conn):
    conn.close()
