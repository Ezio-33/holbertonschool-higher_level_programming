#!/usr/bin/python3
"""Définit une fonction is_same_class qui vérifie
si un objet est exactement une instance d'une classe spécifique"""


def is_same_class(obj, a_class):
    """
    Vérifie si l'objet est exactement une instance de la classe spécifiée.
    et retourne True si l'objet est exactement une instance de la classe
    spécifiée, sinon False.
    """
    return type(obj) is a_class
