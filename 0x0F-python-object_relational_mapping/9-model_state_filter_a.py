#!/usr/bin/python3
'''mysqlalchemy 4'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    pattern = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(pattern.format(sys.argv[1],
                           sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    m = session.query(State).filter(State.name.like('%a%'))
    result = m.order_by(State.id).all()
    for i in result:
        print("{}:".format(i.id), i.name)
    session.close()
