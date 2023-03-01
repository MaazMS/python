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

JobId = 1
JobType = 'Github'
CreatedAt = '14-07-20'
UpdatedAT = '15-07-20'
JobObject = 'synchronize'

# insert values
cur.execute("INSERT INTO repapi VALUES (?,?,?,?,?)", (JobId, JobType, CreatedAt, UpdatedAT, JobObject))
print("insert successfully")


# commit command
con.commit()

# close connection
con.close()



