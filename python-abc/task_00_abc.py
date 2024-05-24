#!/usr/bin/python3


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Méthode abstraite pour produire un son"""
        pass


class Dog(Animal):
    def sound(self):
        """Retourne le son produit par un chien"""
        return "Bark"


class Cat(Animal):
    def sound(self):
        """Retourne le son produit par un chat"""
        return "Meow"
