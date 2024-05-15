#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0] * len(matrix[0]) for _ in matrix]
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            new_matrix[i][j] = elem ** 2
    return new_matrix
