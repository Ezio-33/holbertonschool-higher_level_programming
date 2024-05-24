#!/usr/bin/python3
"""Définit une classe BaseGeometry avec des
méthodes area et integer_validator"""


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

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier et qu'elle est supérieure à 0.

        Args:
            name (str): Le nom de la variable.
            value (int): La valeur à valider.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure ou égale à 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
