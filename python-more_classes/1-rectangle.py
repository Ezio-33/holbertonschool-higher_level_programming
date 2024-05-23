#!/usr/bin/python3
"""Ecrie une classe vide"""


class Rectangle:
    """Definir un rectangle."""

    def __init__(self, width=0, height=0):
        """definir un rectangle
        Args :
        width (int) : largeur du rectangle. La valeur par défaut est 0.
        height (int) : hauteur du rectangle. La valeur par défaut est 0."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """largeur actuelle du rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """la valeur est la longueur du carré"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """hauteur actuelle du rectanglee"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value