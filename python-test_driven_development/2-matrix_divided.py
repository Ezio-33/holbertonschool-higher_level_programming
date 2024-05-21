#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur donné.

    Paramètres:
    matrix (list de listes d'int ou float): La matrice à diviser.
    div (int ou float): Le diviseur.

    Return:
    list de listes de float: Une nouvelle matrice avec les éléments
    divisés par le diviseur.

    Raises: :  TypeError: Si la matrice n'est pas une liste de listes
    d'entiers ou de flottants,
               ou si chaque ligne de la matrice n'a pas la même taille,
               ou si le diviseur n'est pas un nombre.
    ZeroDivisionError: Si le diviseur est égal à zéro.

    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
