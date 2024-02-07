#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """connect to the database"""
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(connection)

    Base.metadata.create_all(engine)
    session = Session(engine)

    cities = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).all()

    for city in cities:
        print("{}: ({}) {}".format(city[0], city.id, city.name))
