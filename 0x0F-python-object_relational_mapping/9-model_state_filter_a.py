#!/usr/bin/python3
"""
A python script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
(using SQLalchemy)
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
    sa = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state_a in sa:
        print("{}: {}".format(state_a.id, state_a.name))
    session.close()
