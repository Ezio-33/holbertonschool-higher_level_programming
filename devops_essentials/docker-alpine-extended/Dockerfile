# syntax=docker/dockerfile:1
FROM alpine:latest

# Installer le paquet curl et nettoyer les fichiers temporaires
RUN apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# Copier le fichier de configuration dans le conteneur
COPY config.txt /app/config.txt

# Définir le point d'entrée par défaut
CMD ["sh"]
