#!/usr/bin/python3
def read_file(filename=""):
    """
    Lit un fichier texte (UTF8) et affiche son contenu sur stdout.

    Args:
        filename (str): Le nom du fichier à lire. Par défaut, une chaîne vide.
    """
    with open(filename, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        print(contenu, end='')
