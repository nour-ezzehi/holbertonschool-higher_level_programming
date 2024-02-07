#!/usr/bin/python3
"""module that contains the class city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, declarative_base
from model_state import Base
Base = declarative_base()


class City(Base):
    """City class that links to the cities table in the MySQL database
    """

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
