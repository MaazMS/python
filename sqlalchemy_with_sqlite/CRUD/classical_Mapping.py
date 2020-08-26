from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Mapper

Engine = create_engine('sqlite:///classical_map.sqlite')
meta_data = MetaData()

Administer = Table('Administer', meta_data,
              Column('id', Integer, primary_key=True),
              Column('Name', String(20)),
              Column('password', String(30))
              )

class Admin():
    def __init__(self, Name, password):
        self.Name= Name
        self.password= password

Mapper(Admin,Administer)
meta_data.create_all(Engine)