#!/usr/bin/python3
"""add a new state in the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
