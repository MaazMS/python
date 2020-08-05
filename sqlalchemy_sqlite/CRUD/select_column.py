from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine('sqlite:///string_and_datetime.sqlite')
Base = declarative_base()
Session_macker = sessionmaker( bind= Engine)
session = Session_macker()

class string_datatime(Base):
    __tablename__ = 'string_datatime'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    created = Column(String(200))

# Base.metadata.create_all(Engine)

print("----> order_by(id):")
select_rows = session.query(string_datatime).order_by(string_datatime.id)
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)

print("\n----> order_by(desc(id)):")
select_rows = session.query(string_datatime).order_by(desc(string_datatime.id))
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)


print("\n----> EQUAL:")
select_rows = session.query(string_datatime).filter(string_datatime.id == 2)
_row = select_rows.first()
print(_row.id, _row.name, _row.created)

print("\n----> NOT EQUAL:")
select_rows = session.query(string_datatime).filter(string_datatime.id != 2)
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)

print("\n----> IN:")
select_rows = session.query(string_datatime).filter(string_datatime.name.in_(['full_name', 'first_name']))
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)

print("\n----> NOT IN:")
select_rows = session.query(string_datatime).filter(~string_datatime.name.in_(['full_name', 'first_name']))
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)

print("\n----> AND:")
select_rows = session.query(string_datatime).filter(string_datatime.name=='full_name', string_datatime.id==5)
_row = select_rows.first()
print(_row.id, _row.name, _row.created)

print("\n----> OR:")
select_rows = session.query(string_datatime).filter(or_(string_datatime.name=='first_name', string_datatime.id==6))
for _row in select_rows.all():
    print(_row.id, _row.name, _row.created)

print("\n----> NULL:")
select_rows = session.query(string_datatime).filter(string_datatime.name == None)
for _row in select_rows.all():
    print(_row.name, _row.created)

print("\n----> NOT NULL:")
select_rows = session.query(string_datatime).filter(string_datatime.name != None)
for _row in select_rows.all():
    print(_row.name, _row.created)

print("\n----> LIKE")
select_rows = session.query(string_datatime).filter(string_datatime.name.like('%name%'))
for _row in select_rows.all():
    print(_row.name, _row.created)