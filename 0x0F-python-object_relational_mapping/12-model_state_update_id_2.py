#!/usr/bin/python3
"""
A python script changes the name of a State object
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                    argv[1],
                                    argv[2],
                                    argv[3]),
                            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_2 = session.query(State).filter_by(id=2).first()
    state_2.name = "New Mexico"
    session.commit()
    session.close()
