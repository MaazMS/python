import sqlite3

con = sqlite3.connect('github.db')

# operation on data base create cursor
cur = con.cursor()


# fetch record fetchone,fetchmany, fetchall
cur.execute("SELECT * FROM repapi ")
print(cur.fetchall())

# commit command
con.commit()

# close connection
con.close()



