#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF8)
    et retourne le nombre de caractères ajoutés.

    Args:
        filename (str): Le nom du fichier dans lequel ajouter le texte.
        Par défaut, une chaîne vide.
        text (str): Le texte à ajouter dans le fichier.
        Par défaut, une chaîne vide.

    Returns:
        int: Le nombre de caractères ajoutés dans le fichier.
    """
    with open(filename, 'a', encoding='utf-8') as fichier:
        nb_caracteres = fichier.write(text)
    return nb_caracteres
