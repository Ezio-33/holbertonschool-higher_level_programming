#!/usr/bin/python3
"""Définit une classe BaseGeometry avec
une méthode area qui lève une exception"""


class BaseGeometry:
    """Classe BaseGeometry"""

    def area(self):
        """
        Méthode qui lève une exception pour indiquer
        que la méthode n'est pas implémentée.

        Raises:
            Exception: avec le message "area() is not implemented"
        """
        raise Exception("area() is not implemented")