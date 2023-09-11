
# Projet de Statistiques sur la Pêche - [fishes_statistic_dashboard]

Ce projet est une plateforme interactive basée sur Django et MongoDB, conçue pour fournir une analyse approfondie des données relatives à différentes espèces dans le domaine de la pêche.

## Description

L'objectif principal de "fishes_statistic_dashboard" est de faciliter la visualisation, l'analyse et l'interprétation des données associées à différentes espèces pêchées. Cette plateforme s'avère cruciale pour les chercheurs, les écologistes et les professionnels de la pêche qui cherchent à comprendre les tendances et les schémas de la pêche dans différentes régions.

## Fonctionnalités 

1. **CRUD Operations:** Permet aux utilisateurs de manipuler les données, à savoir : créer, lire, mettre à jour et supprimer des entrées.
2. **Importation de CSV:** Les utilisateurs peuvent importer des fichiers CSV pour ajouter ou mettre à jour des données en vrac.
3. **Nettoyage des données:** L'outil intégré supprime les doublons et corrige certaines erreurs courantes dans le dataset.
4. **Visualisation:** Des graphiques et des tableaux interactifs pour visualiser les données.
5. [Ajoutez ici d'autres fonctionnalités clés de votre projet]

## Mise en place en local

### Pré-requis:

- Python (Version utilisée: [votre_version])
- MongoDB (Version utilisée: [votre_version])

### Étapes d'installation:

1. Clonez le dépôt sur votre machine:

   ```bash
   git clone [URL_DU_DEPOT]
   ```

2. Naviguez vers le dossier du projet:

   ```bash
   cd fishes_statistic_dashboard
   ```

3. Activez l'environnement virtuel :

   - Sur Windows: 
     ```bash
     venv\Scripts\activate
     ```
   
   - Sur MacOS/Linux: 
     ```bash
     source venv/bin/activate
     ```

4. Installez les dépendances :
   
   ```bash
   pip install -r requirements.txt
   ```

5. Lancez le serveur de développement Django :
   
   ```bash
   python manage.py runserver
   ```

6. Ouvrez un navigateur et naviguez vers `http://127.0.0.1:8000/` pour accéder à l'application.

## Données 

Le dataset se focalise sur l'étude des espèces dans le cadre de la pêche. Il renseigne sur des éléments clés tels que le nom de l'espèce, le volume pêché, la région de pêche, la période de l'année, parmi d'autres informations pertinentes.

## Contribution 

Les contributions sont les bienvenues ! Si vous souhaitez améliorer une fonctionnalité, corriger un bug, ou ajouter une nouvelle fonctionnalité, n'hésitez pas à forker le dépôt, à faire vos modifications et à soumettre une pull request.



## Contact 

Pour toute question, suggestion ou commentaire concernant ce projet, n'hésitez pas à me contacter : hassiba@gmail.com


