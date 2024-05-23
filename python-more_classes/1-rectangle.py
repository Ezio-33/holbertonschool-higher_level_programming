#!/usr/bin/python3
"""Définir une classe Rectangle vide."""

class Rectangle:
    """Définit un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle.
        
        Args:
            width (int): La largeur du rectangle. Par défaut à 0.
            height (int): La hauteur du rectangle. Par défaut à 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur actuelle du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.
        
        Args:
            value (int): La nouvelle largeur du rectangle.
        
        Raises:
            TypeError: Si la largeur n'est pas un entier.
            ValueError: Si la largeur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur actuelle du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.
        
        Args:
            value (int): La nouvelle hauteur du rectangle.
        
        Raises:
            TypeError: Si la hauteur n'est pas un entier.
            ValueError: Si la hauteur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height
