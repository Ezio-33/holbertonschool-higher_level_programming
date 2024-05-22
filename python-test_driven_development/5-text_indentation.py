#!/usr/bin/python3
def text_indentation(text):
    """
    Imprime un texte avec deux nouvelles lignes
    après chaque caractère '.', '?' et ':'.

    Paramètres:
    text (str): Le texte à formater.

    Raise: TypeError: Si text n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result.strip())
