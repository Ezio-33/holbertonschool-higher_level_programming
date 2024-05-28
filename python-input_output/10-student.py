#!/usr/bin/python3
class Student:
    """
    Classe qui définit un étudiant avec des attributs publics.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.
        
        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'instance de Student.
        
        Args:
            attrs (list): Liste optionnelle de noms d'attributs à inclure dans le dictionnaire.
        
        Returns:
            dict: Un dictionnaire contenant les attributs de l'instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}
