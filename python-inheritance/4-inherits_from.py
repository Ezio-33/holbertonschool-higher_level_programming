#!/usr/bin/python3
"""Définit une fonction inherits_from qui vérifie l'héritage d'une classe"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet est une instance d'une classe
    qui a hérité (directement ou indirectement)
    de la classe spécifiée, mais qui n'est pas une
    instance directe de cette classe.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
