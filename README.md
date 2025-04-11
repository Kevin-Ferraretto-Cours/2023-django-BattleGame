# BattleGame

Un mini RPG développé avec Django permettant aux joueurs de créer des comptes, personnaliser leurs personnages, et participer à des combats PvE et PvP en écran partagé.

## 📋 Description

BattleGame est un jeu de rôle web développé avec Django qui offre une expérience immersive où les joueurs peuvent créer leurs propres comptes, personnaliser leurs personnages, acquérir de l'équipement et participer à des combats stratégiques contre des adversaires prédéfinis ou d'autres joueurs en mode écran partagé.

## ✨ Fonctionnalités

- **Système d'Authentification** - Création de compte, connexion et sauvegarde de progression
- **Création et Personnalisation** - Développez un personnage unique avec ses propres attributs
- **Équipement Stratégique** - Choisissez parmi différentes armes et armures pour optimiser votre style de combat
- **Combat PvE** - Affrontez des adversaires prédéfinis aux comportements et difficultés variés
- **Duels PvP** - Défiez d'autres joueurs en mode écran partagé pour déterminer le champion ultime
- **Interface Web Réactive** - Expérience utilisateur fluide et immersive

## 🚀 Installation

```bash
# Cloner le dépôt
git clone https://github.com/Kevin-Ferraretto-Cours/2023-django-BattleGame.git

# Accéder au répertoire
cd 2023-django-BattleGame

# Installation des dépendances
pip install -r requirements.txt

# Configurer la base de données
python manage.py migrate
```

## 🎮 Utilisation

```bash
# Lancer le serveur de développement
python manage.py runserver

# Accéder à l'application dans votre navigateur à l'adresse
# http://127.0.0.1:8000/
```

## 📝 Configuration

Vous pouvez modifier les paramètres de l'application dans le fichier `settings.py`.

Pour un déploiement en production, n'oubliez pas de :
- Définir `DEBUG = False`
- Configurer une clé secrète sécurisée
- Configurer correctement les paramètres de base de données

## 🛠️ Technologies utilisées

- [Django](https://www.djangoproject.com/) - Framework web Python
- [HTML/CSS/JavaScript] - Front-end
- [SQLite/PostgreSQL] - Base de données
- [Tailwind]

## 📈 Roadmap

- Implémentation de classes de personnages supplémentaires
- Ajout d'un système de niveaux et progression
- Développement d'une campagne narrative
- Intégration d'un système de commerce virtuel
- Amélioration des graphismes et de l'interface utilisateur

## 📜 Licence

Ce projet est distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
