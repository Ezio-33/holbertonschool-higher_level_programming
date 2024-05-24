#!/usr/bin/python3
"""Définit une classe Rectangle qui hérite
de BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: L'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation en chaîne
        de caractères de l'objet Rectangle.

        Returns:
            str: La description du rectangle sous
            la forme [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
