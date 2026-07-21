# Partie 1 : Création du module, développement des fonctions, importation et tests du module.

from data_utils import *

# carré de 42

print(carre(42))

#  3 au cube

print(cube(3))

# factorielle de 5

print(factorielle(5))

# valeur absolue de -15

print(valeur_absolue(-15))

# maximum d'une liste 

liste = [10, 5, 8, 12, 3, 7]

print(maximum(liste))


# minimum d'une liste

print(minimum(liste))


# Calcul utilisant toutes les ressours de data_utils

calcul = carre(42) + cube(3) + factorielle(5)/valeur_absolue(-15) - maximum(liste) * minimum(liste)

print(calcul)


# Partie 2 : Création d'un nouveau module, développement des fonctions et test de tâches demandées

from data_utils_V2 import *

# Tâche 1: Test de la fonction somme_cumulee(liste)
# Testez cette fonction avec la liste [5, 10, 15, 20, 25].

liste = [5, 10, 15, 20, 25]
print(somme_cumulee(liste))

# Tâche 2: Test de la fonction `compter_occurrences(liste)
# Testez cette fonction avec la liste ['a', 'b', 'a', 'c', 'b', 'a', 'd'].

liste = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print(compter_occurrences(liste))

# Tâche 4: Test de la fonction inverser_dict(dictionnaire)
# Testez cette fonction avec le dictionnaire {'a': 1, 'b': 2, 'c': 3}.

dictionnaire = {'a': 1, 'b': 2, 'c': 3}
print(inverser_dict(dictionnaire))

# Tâche 5: Test de la fonction filtrer_pairs(liste)
# Testez cette fonction avec la liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrer_pairs(liste))

# Tâche 6: Test de la fonction celsius_to_fahrenheit(celsius)
# Utilisez cette fonction pour convertir les températures suivantes : 0°C, 20°C, 37°C, 100°C.

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

# Tâche 7: Test de la fonction trouver_doublons(liste)
# Testez cette fonction avec la liste [1, 2, 3, 2, 4, 4, 5, 5, 5].

liste = [1, 2, 3, 2, 4, 4, 5, 5, 5]
print(trouver_doublons(liste))

# Tâche 8: Test de la fonction calculer_moyenne_ponderee(valeurs, poids)
# Testez cette fonction avec les listes de valeurs [80, 90, 85, 95] et de poids [0.2, 0.3, 0.3, 0.2].

valeurs = [80, 90, 85, 95]
poids = [0.2, 0.3, 0.3, 0.2]

print(calculer_moyenne_ponderee(valeurs, poids))

# Créez une fonction analyser_texte(texte) qui prend une chaîne de caractères en entrée et retourne un dictionnaire contenant les informations suivantes :

# Nombre total de mots
# Nombre de caractères (espaces inclus)
# Nombre de caractères (espaces exclus)
# Mot le plus long
# Longueur moyenne des mots
# Testez cette fonction avec le texte suivant : 
# "Python est un langage de programmation puissant et facile à apprendre. 
# Il dispose de structures de données de haut niveau efficaces et d'une approche simple mais efficace de la programmation orientée objet."


def analyser_texte(texte):

  mots = texte.split()

  if not mots:
    raise ValueError("La chaîne de caractères est vide.")

  total_mots = len(mots)
  total_caracteres = len(texte)
  total_ch_sans_espaces = len(texte.replace(" ", ""))
  mot_le_plus_long = mots[0]
  
  for mot in mots:
    if len(mot) >= len(mot_le_plus_long):
      mot_le_plus_long = mot

  longueur_moyenne_mots = round((total_ch_sans_espaces / total_mots), 2)

  return {
          "Nombre total de mots": total_mots, 
          "Nombre de caractères (espaces inclus)": total_caracteres,
          "Nombre de caractères (espaces exclus)": total_ch_sans_espaces,
          "Mot le plus long": mot_le_plus_long,
          "Longueur moyenne des mots": longueur_moyenne_mots
          }

texte = "Python est un langage de programmation puissant et facile à apprendre. Il dispose de structures de données de haut niveau efficaces et d'une approche simple mais efficace de la programmation orientée objet."

print(analyser_texte(texte))
