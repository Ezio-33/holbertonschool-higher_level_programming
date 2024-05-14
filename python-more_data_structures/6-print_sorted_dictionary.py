#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    liste_trie = sorted(a_dictionary.keys())
    for key in liste_trie:
        print(key, ": ", a_dictionary[key])
