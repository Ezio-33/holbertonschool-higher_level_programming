#!/usr/bin/python3
"""fonction pour ajouter des arguments
de ligne de commande à un fichier JSON."""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_json():
    """
    Ce script ajoute des arguments de ligne de commande à un fichier JSON.

    Il vérifie si le fichier existe et charge la liste existante,
    sinon, il crée une nouvelle liste. Il ajoute ensuite les arguments
    de la ligne de commande à la liste et enregistre la liste mise à jour.
    """
    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)


add_items_to_json()
