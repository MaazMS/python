from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import datetime as dt


Engine = create_engine('sqlite:///string_and_datetime.sqlite')
Base = declarative_base()
Session = sessionmaker(bind = Engine)
session = Session()

class string_datatime(Base):
    __tablename__ = 'string_datatime'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    created = Column(String(200))

# Base.metadata.create_all(Engine)



year  = 2020
month = 8
day   = 5
hour  = 2
mint  = 50
sec   = 00
createdatatime = datetime.datetime(year, month, day, hour, mint, sec )
print(createdatatime)
datatime_string =createdatatime.strftime("%d-%m-%Y %H:%M:%S")
print(datatime_string)
create_datatime = datetime.datetime(year, month, day, hour, mint, sec ) + dt.timedelta(seconds=20)
print(create_datatime)
datatime_string =create_datatime.strftime("%d-%m-%Y %H:%M:%S")
print(datatime_string)





object_string_datatime = string_datatime( created = datatime_string )

session.add(object_string_datatime)
session.commit()
print("insert successfull")

#  This line is use after 20.  To convert datatime to string form and pass to column name
# datatime_string =data_time.strftime("%d-%m-%Y %H:%M:%S")