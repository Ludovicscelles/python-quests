# Modules Python

# Avec Python, on est souvent amené à travailler avec des données complexes et devoir effectuer du code répétitif.
# Les modules Python sont des outils essentiels pour optimiser et étendre les capacités de base de Python.

# Un module en Python est simplement un fichier contenant du code Python.
# Il peut contenir des fonctions, des classes et des variables que vous pouvez utiliser dans votre propre code.
# Par exemple, la fonction print() que vous utilisez fréquemment fait partie du module standard de Python.

# Pourquoi utiliser des modules ?

# 1. Réutilisation du code : Les modules permettent de réutiliser du code existant, ce qui réduit la duplication et facilite la maintenance.

# 2. Organisation du code : Les modules permettent de structurer le code en différentes parties, ce qui rend le code plus lisible et plus facile à comprendre.

# 3. Fonctionnalités avancées : Les modules offrent des fonctionnalités avancées qui ne sont pas disponibles dans le langage de base, comme la manipulation de fichiers, la gestion des dates et heures, et bien plus encore.

# 4. Maintenance facilitée : Les modules permettent de mettre à jour et de corriger le code plus facilement, car les modifications peuvent être apportées dans un seul endroit.

# 5. Collaboration : Les modules facilitent la collaboration entre les développeurs, car chacun peut travailler sur des modules spécifiques sans interférer avec le code des autres.


# Modules standards

# Python vient avec une bibliothèque standard riche en modules qui couvrent un large éventail de fonctionnalités. 

# Voici quelques exemples de modules standards populaires :

# 1. Module math : Fournit des fonctions mathématiques avancées, telles que les fonctions trigonométriques, les logarithmes et les constantes mathématiques.

# exemple d'utilisation du module math :

import math

# Variable

print(math.pi)  # Affiche la valeur de pi
print(math.e)   # Affiche la valeur de e
print()

# Fonctions mathématiques
print(math.sqrt(16))  # Affiche la racine carrée de 16
print(math.log(98, 10))  # Affiche le logarithme de 100 en base 10
print(math.sin(math.pi / 2))  # Affiche le sinus de pi/2
print()

# 2. Module random : Permet de générer des nombres aléatoires et de sélectionner des éléments de manière aléatoire.

import random

# Fonctions du module random
print(random.randint(1, 10))  # Affiche un nombre aléatoire entre 1 et 10
print(random.choice(['chocolat_noir_noisette', 'chocolat_au_lait_amandes', 'chocolat_blanc_riz_soufflé']))  # Affiche un élément aléatoire de la liste
print(random.sample(range(1, 100), 5))  # Affiche 5 nombres aléatoires uniques entre 1 et 100
print()

# 3. Module datetime : Permet de travailler avec les dates et les heures.

import datetime

# Variable
now = datetime.datetime.now()  # Récupère la date et l'heure actuelles
print(now)  # Affiche la date et l'heure actuelles
print(now.year)  # Affiche l'année actuelle
print(now.month)  # Affiche le mois actuel
print()
today = datetime.date.today()  # Récupère la date actuelle sans l'heure
print(today)  # Affiche la date actuelle sans l'heure
print()


# Fonctions du module datetime
future_date = today + datetime.timedelta(days=7)  # Calcule la date dans 7 jours
print(future_date)  # Affiche la date dans 7 jours
print()


# 4. Module statistics : Fournit des fonctions pour effectuer des calculs statistiques de base, comme la moyenne, la médiane et l'écart type.

import statistics

# Liste de nombres
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Fonctions du module statistics
print(statistics.mean(data))  # Affiche la moyenne des nombres
print(statistics.median(data))  # Affiche la médiane des nombres
print(statistics.mode(data))  # Affiche le mode des nombres
print(statistics.stdev(data))  # Affiche l'écart type des nombres
print()


# Modules externes

# Ce sont des modules créés par la communauté Python pour des besoins spécifiques. 
# Ils ne font pas partie de la bibliothèque standard et doivent être installés séparément.

# Exemples de modules externes populaires :

# 1. pandas : Une bibliothèque puissante pour la manipulation et l'analyse de données, 
# offrant des structures de données flexibles et des outils pour travailler avec des tableaux et des séries temporelles.

# 2. numpy : Une bibliothèque pour le calcul scientifique, offrant des fonctionnalités avancées pour les tableaux multidimensionnels 
# et les opérations mathématiques.

# 3. matplotlib : Une bibliothèque pour la création de visualisations de données, permettant de générer des graphiques et des diagrammes.


#  Comment utiliser un module ?

# 1. Importer tout le module : Vous pouvez importer un module entier en utilisant l'instruction import.

# Exemple :

import math

result = math.sqrt(16)  # Utilisation de la fonction sqrt() du module math

# 2. Importer une fonction spécifique : Vous pouvez importer une fonction spécifique d'un module en utilisant l'instruction from ... import.

from math import sqrt

result = sqrt(16)  # Utilisation de la fonction sqrt() directement sans préfixe

# 3. Importer un module avec un alias : Vous pouvez donner un alias à un module lors de l'importation en utilisant l'instruction as.

import math as m

result = m.sqrt(16)  # Utilisation de la fonction sqrt() avec l'alias m

# 4. Importer plusieurs fonctions spécifiques : Vous pouvez importer plusieurs fonctions spécifiques d'un module en les séparant par des virgules.

from math import sqrt, pi, sin

result = sqrt(16)  # Utilisation de la fonction sqrt()
angle = pi / 2  # Utilisation de la constante pi
result_sin = sin(angle)  # Utilisation de la fonction sin()


# Utilisation d'un module personnalisé


from my_modules import *

courses = ["History", "Math", "Physics", "CompSci"]

index = find_index(courses, "Math")
print(f"Index of 'Math' in courses: {index}")
print(f"Test variable from my_modules: {test}")

import sys

print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")
print(sys.path)  # Affiche la liste des chemins de recherche des modules
print()

# Imaginons que nous ayons des données de ventes mensuelles

ventes = [1000, 1200, 950, 1100, 1300, 1050, 1150, 1250, 1100, 1200, 1300, 1400]

print(f"Moyenne des ventes: {mean(ventes)}")
print(f"Médiane des ventes: {median(ventes)}")
print(f"Écart type des ventes: {ecart_type(ventes)}")

ventes_normalisées = normalize_data(ventes)
print(f"Ventes normalisées: {round_list(ventes_normalisées, 2)}")

croissance_annuelle = growth_rate(ventes[0], ventes[-1])
print(f"Taux de croissance annuel: {croissance_annuelle:.2f}%")

mois_plus_ventes = YEAR_MONTHS[ventes.index(max(ventes))]
print(f"Mois avec le plus de ventes: {mois_plus_ventes}")

# Imaginons des données avec des valeurs manquantes
donnees_brutes = [1000, 1200, None, 1100, '', 1050, 1150, None, 1100, 1200, '', 1400]
donnees_nettoyees = clear_data(donnees_brutes)
print(f"Données nettoyées: {donnees_nettoyees}")

# Analyse de la fréquence 
categories = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'B']
frequence_relative = relative_frequency(categories)
print(f"Fréquence relative des catégories: {frequence_relative}")
print(f"Catégorie la plus fréquente: {find_mode(categories)}")










