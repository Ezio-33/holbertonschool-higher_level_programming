#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for cpt in range(len(matrix)):
        new[cpt] = list(map(lambda x: x**2, matrix[cpt]))

    return (new)
