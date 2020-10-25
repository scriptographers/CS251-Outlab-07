import sqlite3 as sql

with open('University Schema', 'r') as file:
    crt = file.read()
with open('smallRelationsInsertFile.sql', 'r') as file:
    ins = file.read()
DB_NAME = "univ.db"

conn = sql.connect(DB_NAME)
cur = conn.cursor()

for x in crt.split(';') + ins.split(';'):
    try:
        cur.execute(x)
        conn.commit()
    except Exception as error:
        continue

cur.close()

if (conn):
    conn.close()
