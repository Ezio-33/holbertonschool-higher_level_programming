#!/usr/bin/python3
"""
Liste tous les objets State qui contiennent la lettre 'a' de la base de données hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    nom_utilisateur = sys.argv[1]
    mdp = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        nom_utilisateur, mdp, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
