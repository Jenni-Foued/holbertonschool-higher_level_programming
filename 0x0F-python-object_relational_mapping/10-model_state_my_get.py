#!/usr/bin/python3
"""
A python script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
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
    query = session.query(State).filter(State.name.like(argv[4],)).first()
    if query is None:
        print("Not found")
    else:
        print("{}".format(query.id))
    session.close()
