#!/usr/bin/python3
"""
Affiche l'objet State dont le nom est passé en argument
de la base de données hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    nom_utilisateur = sys.argv[1]
    mdp = sys.argv[2]
    database = sys.argv[3]
    nom_etat = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        nom_utilisateur, mdp, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == nom_etat).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
