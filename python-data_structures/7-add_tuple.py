#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # Remplir les tuples avec des zéros s'ils sont vide
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Ajouter les premiers éléments de chaque tuple
    sum_1 = tuple_a[0] + tuple_b[0]

    # Ajouter les deuxièmes éléments de chaque tuple
    sum_2 = tuple_a[1] + tuple_b[1]

    # Retourne le tuple résultant
    return (sum_1, sum_2)
