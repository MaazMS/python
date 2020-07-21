from sqlalchemy_sqlite.CRUD.declarative_map import Customer , Engine
from  sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind= Engine)
session = Session()

cust_name = input('Enter customer name')
cust1 = Customer(name = cust_name)
session.add(cust1)
session.commit()
print('insert successful')