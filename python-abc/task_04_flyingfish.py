#!/usr/bin/python3

class Fish:
    def swim(self):
        """Affiche que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("The fish lives in water")


class Bird:
    def fly(self):
        """Affiche que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def swim(self):
        """Affiche que le poisson volant nage."""
        print("The flying fish is swimming!")

    def fly(self):
        """Affiche que le poisson volant plane."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Affiche l'habitat du poisson volant."""
        print("The flying fish lives both in water and the sky!")
