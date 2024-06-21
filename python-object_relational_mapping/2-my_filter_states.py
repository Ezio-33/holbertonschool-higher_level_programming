#!/usr/bin/python3
"""
Se connecte à une base de données MySQL et
affiche toutes les valeurs de la table "states"
où le nom correspond à l'argument fourni.

Args :
username (str): Le nom d'utilisateur pour la base de données MySQL.
password (str): Le mot de passe de la base de données MySQL.
database (str): Le nom de la base de données MySQL.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    select = """SELECT * FROM states WHERE name = '{}'
ORDER BY id ASC""".format(state_name_searched)
    cursor.execute(select)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
