#!/usr/bin/python3
"""Définit une fonction is_kind_of_class qui vérifie si un objet
est une instance d'une classe spécifiée ou d'une classe qui en hérite"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de la classe
    spécifiée ou d'une classe qui en hérite.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

    Returns:
        True si l'objet est une instance de la classe spécifiée
        ou d'une classe qui en hérite, False sinon.
    """
    return isinstance(obj, a_class)
