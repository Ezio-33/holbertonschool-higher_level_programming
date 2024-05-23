#!/usr/bin/python3
"""Définir une classe Rectangle avec des attributs privés
et des méthodes pour calculer l'aire et le périmètre."""

class Rectangle:
    """Définit un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une 
        largeur et une hauteur optionnelles.
        
        Args:
            width (int): La largeur du rectangle. La valeur par défaut est 0.
            height (int): La hauteur du rectangle. La valeur par défaut est 0.
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle.
        
        Returns:
            int: L'aire du rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle,
            ou 0 si l'une des dimensions est 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
