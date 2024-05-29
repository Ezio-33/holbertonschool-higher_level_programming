#!/usr/bin/env python3
"""Sérialise et charge des données à partir d'un fichier JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python en JSON et l'enregistre dans un fichier.

    :param data: Dictionnaire Python à sérialiser
    :param filename: Nom du fichier de sortie JSON
    :param indent: Indentation du fichier JSON pour une meilleur lisible.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et désérialise son contenu
    en un dictionnaire Python.

    :param filename: Nom du fichier JSON d'entrée
    :return: Dictionnaire Python désérialisé
    """
    with open(filename, 'r') as file:
        return json.load(file)
