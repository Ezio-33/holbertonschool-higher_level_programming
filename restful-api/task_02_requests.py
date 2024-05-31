#!/usr/bin/python3
import requests
import json


def fetch_and_print_posts():
    """Envoyer une requête GET à l'API JSONPlaceholder"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    """Afficher le code de statut de la réponse"""
    print(f'Status Code: {response.status_code}')

    """Si la requête a réussi, traiter les données JSON"""
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Envoyer une requête GET à l'API JSONPlaceholder"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    """Si la requête a réussi, traiter les données JSON"""
    if response.status_code == 200:
        posts = response.json()
        """Structurer les données en une liste de dictionnaires"""
        data = [{'id': post['id'], 'title': post['title'],
                 'body': post['body']} for post in posts]

        """Écrire les données dans un fichier CSV"""
        import csv
        with open('posts.csv', 'w', newline='') as csvfichier:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfichier, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
