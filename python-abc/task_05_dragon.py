#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        """Affiche que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """Affiche que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """Affiche que le dragon rugit."""
        print("The dragon roars!")
