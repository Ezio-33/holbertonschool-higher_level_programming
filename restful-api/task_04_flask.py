#!/usr/bin/python3
from flask import Flask, jsonify, request

""" Crée une instance de l'application Flask"""
app = Flask(__name__)

""" Initialise un dictionnaire vide pour stocker les utilisateurs"""
users = {}


@app.route("/")
def home():
    """
    Cette fonction gère la route racine de l'API Flask.
    Return:
            str: Un message de bienvenue pour l'API Flask.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Récupère une liste de noms d'utilisateur du dictionnaire 'users'
    et la retourne sous forme de réponse JSON.
    Return:
            Une réponse JSON contenant une liste de noms d'utilisateur.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Retourne le statut de l'API.
    Return:
            str: Le message de statut "OK".
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Récupère les informations de l'utilisateur
    basé sur le nom d'utilisateur fourni.
    Args:
            username: Le nom d'utilisateur de l'utilisateur
            pour lequel récupérer les informations.
    Return:
            Si l'utilisateur est trouvé, les informations de l'utilisateur
            sont retournées sous forme de réponse JSON.
            Si l'utilisateur n'est pas trouvé, une réponse JSON avec un
            message d'erreur et un code de statut 404 est retournée.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur au système.
    Return:
            Une réponse JSON avec la structure suivante:
            - Si les données JSON sont invalides:
            {"error": "Invalid JSON data"}
            - Si le nom d'utilisateur existe déjà:
            {"error": "Username already exists"}
            - Si l'utilisateur est ajouté avec succès:
            {"message": "User added", "user": <user_data>}
            - Si une exception se produit: {"error": <exception_message>}
    """
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = new_user
    return jsonify({"message": "User added", "user": users[username]}), 201


""" Démarre le serveur Flask lorsque le script est exécuté directement"""
if __name__ == "__main__":
    app.run()
