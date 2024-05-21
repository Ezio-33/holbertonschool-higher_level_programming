#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Imprime "My name is <first name> <last name>".

    Paramètres:
    first_name (str): Le prénom. Doit être une chaîne de caractères.
    last_name (str, optionnel): Le nom de famille. Doit être une chaîne
    de caractères. Par défaut, c'est une chaîne vide.

    Raise: TypeError: Si first_name ou last_name
    ne sont pas des chaînes de caractères.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
