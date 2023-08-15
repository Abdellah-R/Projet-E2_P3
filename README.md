# Application web pour prédire le prix d'une maison

## [![Docker Build](https://img.shields.io/docker/cloud/build/votre-utilisateur/votre-projet)](https://hub.docker.com/r/votre-utilisateur/votre-projet)
[![Django Version](https://img.shields.io/badge/django-4.2-green.svg)](https://docs.djangoproject.com/en/4.2/)

## Description

Cette application Web Django vise à prédire les prix de l'immobilier en fonction des caractéristiques de la maison. Il fournit une interface utilisateur conviviale et permet de saisir les caractéristiques de la maison et d'obtenir une estimation du prix de la propriété. Le modèle de prédiction est formé sur un ensemble de données de ventes immobilières, incorporant divers facteurs tels que l'emplacement, la superficie, le nombre de pièces, etc., pour faire des prédictions précises.

![](data/screenshot.png)

## Guide

Pour lancer l'application web localement, suivez ces étapes:

1. Placez-vous dans le premier répertoire real_estate_app à partir de la racine:
```bash
cd real_estate_app
```

2. Utilisez cette commande pour construire l'image docker:

```bash
docker build -t django-app .
```

3. Exécuter le conteneur en mappant les ports et en montant un volume:

```bash
docker run -dp 8000:8000 -v "$PWD":/app django-app
```

L'application sera accessible à l'adresse http://0.0.0.0:8000/ dans votre navigateur.

