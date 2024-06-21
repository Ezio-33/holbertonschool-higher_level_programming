#!/usr/bin/python3
"""
Se connecte à une base de données MySQL et
liste toutes les villes d'un état spécifique de la table "cities"
de la base de données "hbtn_0e_4_usa".

Args :
    nom_utilisateur (str) : Le nom d'utilisateur de la base de données MySQL.
    mdp (str) : Le mot de passe de la base de données MySQL.
    database (str) : Le nom de la base de données.
    nom_etat (str) : Le nom de l'état dont on veut lister les villes.
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
    select = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(select, (nom_etat,))

    cities = cursor.fetchall()

    nom_ville = [city[0] for city in cities]
    print(", ".join(nom_ville))

    cursor.close()
    db.close()
