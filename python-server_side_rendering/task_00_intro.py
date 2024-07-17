#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    """
    Génère des fichiers d'invitation personnalisés à partir d'un modèle et d'une liste de participants.
    
    Args:
        template (str): Le modèle d'invitation avec des espaces réservés.
        attendees (list): Liste de dictionnaires contenant les informations des participants.
        
    Returns:
        None
    """

    if not isinstance(template, str):
        print("Erreur: Le modèle doit être une chaîne de caractères.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur: Les participants doivent être une liste de dictionnaires.")
        return
    
    if not template.strip():
        print("Erreur: Le modèle est vide, aucun fichier de sortie généré.")
        return
    if not attendees:
        print("Erreur: Aucun participant fourni, aucun fichier de sortie généré.")
        return
    

    for i, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, "N/A")
            invitation = invitation.replace(f"{{{key}}}", value if value else "N/A")
        
        output_file = f'output_{i}.txt'

        if os.path.exists(output_file):
            print(f"Erreur: {output_file} existe déjà. Ignoré.")
            continue
        

        try:
            with open(output_file, 'w') as file:
                file.write(invitation)
            print(f"Fichier généré: {output_file}")
        except Exception as e:
            print(f"Erreur lors de l'écriture dans {output_file}: {e}")

