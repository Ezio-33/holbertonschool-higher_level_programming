#!/usr/bin/python3


class VerboseList(list):
    def append(self, item):
        """Ajoute un élément à la liste et
        affiche un message de notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étend la liste avec les éléments d'un itérable
        et affiche un message de notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Supprime un élément de la liste et affiche
        un message de notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Supprime et retourne un élément de la liste et
        affiche un message de notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
