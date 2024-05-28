#!/usr/bin/python3
"""Fonction pour convertir un objet en chaîne JSON."""
import json


def to_json_string(my_obj):
    """
    Retourne la représentation JSON d'un objet (chaîne de caractères).

    Args:
        my_obj: L'objet à convertir en chaîne JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """
    return json.dumps(my_obj)
