import sqlite3
con = sqlite3.connect('github.db')

# operation on data base create cursor
cur = con.cursor()

# create table
cur.execute("""CREATE TABLE IF NOT EXISTS repapi (
        JobId INTEGER,
        JobType TEXT,
        CreatedAt TEXT,
        UpdatedAT TEXT,
        JobObject TEXT
        )""")
print("table is created ")

con.commit()
con.close()