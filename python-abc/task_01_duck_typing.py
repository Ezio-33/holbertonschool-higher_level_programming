#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Retourne l'aire du cercle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Retourne le périmètre du cercle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre de la forme"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
