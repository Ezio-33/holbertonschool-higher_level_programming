#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    Crée un objet à partir d'un fichier JSON.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        object: La structure de données Python représentée par le fichier JSON.
    """
    with open(filename, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)
