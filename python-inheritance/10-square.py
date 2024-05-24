#!/usr/bin/python3
"""Définit une classe Square qui hérite de Rectangle (9-rectangle.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square qui hérite de Rectangle"""

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du carré.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'objet Square.

        Returns:
            str: La description du carré sous la forme [Rectangle] <size>/<size>.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
