#!/usr/bin/env python3
"""Sérialise et charge des données à partir d'un fichier JSON."""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialise un objet CustomObject avec les attributs spécifiés.

        :param name: Nom de l'objet (str)
        :param age: Âge de l'objet (int)
        :param is_student: Statut étudiant de l'objet (bool)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de l'objet et
        l'enregistre dans le fichier spécifié.

        :param filename: Nom du fichier où l'objet sera sérialisé (str)
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet à partir du fichier spécifié et
        retourne une instance de CustomObject.

        :param filename: Nom du fichier d'où l'objet sera désérialisé (str)
        :return: Instance de CustomObject ou None en cas d'erreur
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, Exception) as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
