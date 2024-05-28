#!/usr/bin/python3
"""Fonction pour générer un triangle de Pascal."""


def pascal_triangle(n):
    """
    Retourne une liste de listes d'entiers représentant
    le triangle de Pascal de profondeur n.

    Args:
        n (int): La profondeur du triangle de Pascal.

    Returns:
        list: Une liste de listes d'entiers représentant le triangle de Pascal.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
