#!/usr/bin/python3
"""This module contain a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided function divides all elements of a matrix

    Args:
    matrix (list of lists): two dimension matrix
    div (int, float): divisor

    Returns:
        list of lists: all elements divided inside a new matrix
    
    Raises:
    TypeError: If the matrix is not a list of integer or float
    of integers or floats,
               or if each row of the matrix does not have the same size,
               or if the divisor is not a number.
    ZeroDivisionError: If the divisor is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or matrix == []:
        raise TypeError(error)

    # capture the first row len
    len_row = len(matrix[0])

    # validate div conditions
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # validate rows len in matrix and values inside each list
    for idx in matrix:
        if type(idx) != list or idx == []:
            raise TypeError(error)
        if len(idx) == len_row:
            for j in idx:
                if type(j) != int and type(j) != float:
                    raise TypeError(error)
        else:
            raise TypeError(
                    "Each row of the matrix must have the same size")
    mat_code = map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix)

    return list(mat_code)