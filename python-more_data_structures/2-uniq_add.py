#!/usr/bin/python3
def uniq_add(my_list=[]):
    liste_unique = set(my_list)
    num = 0

    for i in liste_unique:
        num += i

    return (num)
