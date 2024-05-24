#!/usr/bin/python3
"""Module pour définir une classe MyList qui hérite de list"""


class MyList(list):
    """Classe MyList qui hérite de list"""

    def print_sorted(self):
        """Imprime la liste triée (ordre croissant)"""
        print(sorted(self))
