#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Retourne un objet (structure de données Python) représenté par une chaîne JSON.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        object: La structure de données Python représentée par la chaîne JSON.
    """
    return json.loads(my_str)
