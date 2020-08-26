from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.sqlite')
connection = engine.connect()

try:
    print("your connection is ok and connection object is {}".format(connection))
except:
    print("your not connect to database")