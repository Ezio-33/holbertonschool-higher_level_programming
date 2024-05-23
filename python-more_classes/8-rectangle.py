#!/usr/bin/python3
"""Définir une classe Rectangle avec des attributs privés,
des méthodes pour calculer l'aire et le périmètre,
et pour afficher le rectangle, ainsi qu'un compteur d'instances."""


class Rectangle:
    """Définit un rectangle."""

    # Attributs de classe
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur
        optionnelles.

        Args:
            width (int): La largeur du rectangle. La valeur par défaut est 0.
            height (int): La hauteur du rectangle. La valeur par défaut est 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Retourne une chaîne de caractères représentant le rectangle
        avec le caractère(s) stocké(s) dans print_symbol.

        Returns:
            str: Représentation du rectangle avec des print_symbol,
            ou une chaîne vide si l'une des dimensions est 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)]
        )

    def __repr__(self):
        """Retourne une chaîne de caractères représentant
        l'objet Rectangle, qui peut être utilisée pour recréer l'objet.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Affiche un message lors de la suppression d'une instance de
        Rectangle et décrémente le compteur d'instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le plus grand rectangle basé sur l'aire.

        Args:
            rect_1 (Rectangle): Le premier rectangle.
            rect_2 (Rectangle): Le deuxième rectangle.

        Raises:
            TypeError: Si rect_1 ou rect_2 ne sont pas des instances de
            Rectangle.

        Returns:
            Rectangle: Le rectangle avec la plus grande aire, ou rect_1 si
            les aires sont égales.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
