from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Engine = create_engine('sqlite:///string_and_datetime.sqlite')
Base = declarative_base()
Session = sessionmaker(bind = Engine)
session = Session()

class string_datatime(Base):
    __tablename__ = 'string_datatime'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    created = Column(DateTime)

Base.metadata.create_all(Engine)

data_time = datetime.now()
print(data_time)

object_string_datatime = string_datatime(name = 'first_name' , created = data_time )

session.add(object_string_datatime)
session.commit()
print("insert successfull")

#  This line is use after 20.  To convert datatime to string form and pass to column name
# datatime_string =data_time.strftime("%d-%m-%Y %H:%M:%S")