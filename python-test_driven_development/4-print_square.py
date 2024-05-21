#!/usr/bin/python3
def print_square(size):
    """
    Imprime un carré de taille donnée avec le caractère '#'.

    Paramètres:
    size (int): La taille du carré.

    Raise:
    TypeError: Si size n'est pas un entier.
    ValueError: Si size est inférieur à 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
