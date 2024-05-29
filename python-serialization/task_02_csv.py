#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en JSON et écrit les données dans data.json.

    :param csv_filename: Nom du fichier CSV à convertir (str)
    :return: True si la conversion est réussie, False sinon
    """
    try:

        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Erreur : Le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
