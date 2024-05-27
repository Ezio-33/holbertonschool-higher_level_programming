#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF8)
    et retourne le nombre de caractères écrits.

    Args:
        filename (str): Le nom du fichier dans lequel écrire.
        Par défaut, une chaîne vide.
        text (str): Le texte à écrire dans le fichier.
        Par défaut, une chaîne vide.

    Returns:
        int: Le nombre de caractères écrits dans le fichier.
    """
    with open(filename, 'w', encoding='utf-8') as fichier:
        nb_caracteres = fichier.write(text)
    return nb_caracteres
