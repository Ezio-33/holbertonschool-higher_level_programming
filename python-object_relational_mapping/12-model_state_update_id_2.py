#!/usr/bin/python3
"""
Modifie le nom de l'objet State dont l'ID est 2 en 
"New Mexico" dans la base de données hbtn_0e_6_usa.
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

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
