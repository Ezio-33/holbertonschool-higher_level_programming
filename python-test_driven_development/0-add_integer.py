#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Cette fonction ajoute deux nombres entiers ou flottants après les avoir convertis en entiers.
    Si a ou b ne sont pas des entiers ou des flottants, une exception TypeError est faite.

    Paramètres:
    a : Le premier nombre à ajouter. Doit être un entier ou un flottant.
    b : Le deuxième nombre à ajouter. Doit être un entier ou un flottant. Par défaut à 98.

    Return:
    int: La somme de a et b après conversion en entiers.

    Raises: TypeError: Si a ou b ne sont pas des entiers ou des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
