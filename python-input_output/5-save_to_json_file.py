#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier texte en utilisant une représentation JSON.

    Args:
        my_obj: L'objet à écrire dans le fichier.
        filename (str): Le nom du fichier dans lequel écrire l'objet.
    """
    with open(filename, 'w', encoding='utf-8') as fichier:
        json.dump(my_obj, fichier)
