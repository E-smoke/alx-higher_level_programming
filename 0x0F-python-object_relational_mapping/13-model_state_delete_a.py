#!/usr/bin/python3
'''sqlalchemy 3'''


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
    obj = session.query(State).filter(State.name.like('%a%')).all()
    for i in obj:
        session.delete(i)
    session.commit()
    session.close()
