#!/usr/bin/python3
"""
Se connecte à une base de données MySQL et
sélectionne tous les états de la table "states".

Args :
    nom_utilisateur (str) : Le nom d'utilisateur de la base de données MySQL.
    mdp (str) : Le mot de passe de la base de données MySQL.
    database (str) : Le nom de la base de données.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()