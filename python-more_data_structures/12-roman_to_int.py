#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_valeurs = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    resultat = 0
    prev_valeur = 0

    for char in roman_string[::-1]:
        valeur = roman_valeurs[char]
        if valeur >= prev_valeur:
            resultat += valeur
        else:
            resultat -= valeur
        prev_valeur = valeur

    return resultat
