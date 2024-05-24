#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        """Initialise l'itérateur et le compteur."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Incrémente le compteur et retourne le prochain élément."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Retourne le nombre d'éléments itérés."""
        return self.counter
