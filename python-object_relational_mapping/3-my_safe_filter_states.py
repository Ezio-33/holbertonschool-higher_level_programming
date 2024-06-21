#!/usr/bin/python3
"""
Se connecte à une base de données MySQL et
affiche toutes les valeurs de la table "states"
où le nom correspond à l'argument fourni.

Args :
    nom_utilisateur (str) : Le nom d'utilisateur de la base de données MySQL.
    mdp (str) : Le mot de passe de la base de données MySQL.
    database (str) : Le nom de la base de données.
    nom_etat (str) : Le nom de l'état à rechercher.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    nom_utilisateur = sys.argv[1]
    mdp = sys.argv[2]
    database = sys.argv[3]
    nom_etat = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=nom_utilisateur,
        passwd=mdp,
        db=database
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (nom_etat,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
