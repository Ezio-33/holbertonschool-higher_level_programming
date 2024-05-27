#!/usr/bin/python3
def class_to_json(obj):
    """
    Retourne la description d'un objet sous forme de
    dictionnaire avec des structures de données simples.

    Args:
        obj: L'objet à convertir en dictionnaire.

    Returns:
        dict: La description de l'objet sous forme de dictionnaire.
    """
    return (obj.__dict__)
