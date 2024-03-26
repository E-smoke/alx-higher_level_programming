#!/usr/bin/python3
'''mysqlalchemy 2'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


pattern = "mysql://{}:{}@localhost/{}"
engine = create_engine(pattern.format(sys.argv[1], sys.argv[2], sys.argv[3]))
Session = sessionmaker(bind=engine)
session = Session()
state = session.query(State).order_by(State.id).all()
for i in state:
    print("{}:".format(i.id), i.name)
session.close()
