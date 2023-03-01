from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import  declarative_base


Engine = create_engine('sqlite:///declarative_map.sqlite')
BASE = declarative_base()  # This base class have configuration

# create Table
# inherit form base class
class Customer(BASE):
    __tablename__ ='Customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))

# important
BASE.metadata.create_all(Engine)