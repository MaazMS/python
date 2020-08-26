import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()


class Test(DeclarativeBase):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine('sqlite:///datetime_column.sqlite')
DeclarativeBase.metadata.create_all(engine)
session_maker = sessionmaker(engine)
session = session_maker()


tes1 = Test()
session.add(tes1)
session.commit()

print(tes1.created)