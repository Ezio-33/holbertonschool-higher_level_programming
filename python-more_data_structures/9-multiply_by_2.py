#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionnaire = a_dictionary.copy()
    list_keys = list(new_dictionnaire.keys())

    for i in list_keys:
        new_dictionnaire[i] *= 2

    return (new_dictionnaire)
