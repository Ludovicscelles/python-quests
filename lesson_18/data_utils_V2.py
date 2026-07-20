# Functions

# somme_cumulee(liste): calcule la somme cumulée d'une liste et retourne une liste. 
# Par exemple, pour la liste [1, 2, 3, 4], la somme cumulée serait [1, 3, 6, 10].

def somme_cumulee(liste):

  if not liste:
    raise ValueError("La liste est vide.")
  
  resultat = []
  somme = 0
  
  for nombre in liste:
    somme += nombre
    resultat.append(somme)

  return resultat

# compter_occurrences(liste): retourne un dictionnaire contenant le nombre d'occurrences de chaque élément de la liste. 
# Par exemple, pour la liste [1, 2, 2, 3], le résultat serait {1: 1, 2: 2, 3: 1}.

def compter_occurrences(liste):

  if not liste:
    raise ValueError("La liste est vide.")
  
  counts = {}

  for value in liste:
    if value in counts:
      counts[value] += 1
    else:
      counts[value] = 1

  return counts


# inverser_dict(dictionnaire): inverse les clés et les valeurs d'un dictionnaire. 
# Par exemple, pour le dictionnaire {'a': 1, 'b': 2}, le résultat serait {1: 'a', 2: 'b'}.

def inverser_dict(dictionnaire):

  if not dictionnaire:
    raise ValueError("Le dictionnaire est vide.")
  
  dictionnaire_inverse = {}
  
  for key, value in dictionnaire.items():
    dictionnaire_inverse[value] = key
  
  return dictionnaire_inverse


# filtrer_pairs(liste): retourne une nouvelle liste contenant uniquement les nombres pairs de la liste d'entrée. 
# Par exemple, pour la liste [1, 2, 3, 4], le résultat serait [2, 4].

def filtrer_pairs(liste):
  
  nombres_pairs = []

  for nombre in liste:
    if nombre % 2 == 0:
      nombres_pairs.append(nombre)

  return nombres_pairs

liste = [1, 2, 3, 4, 5, 6]


# celsius_to_fahrenheit(celsius): convertit une température de Celsius en Fahrenheit et retourne un nombre. 
# Par exemple, pour une température de 0°C, le résultat serait 32°F. Rappel : la formule est F = (C * 9/5) + 32

def celsius_to_fahrenheit(celsius):
  return f"Pour une température de {celsius}°C, la conversion en Fahrenheit est : {(celsius * 9/5) + 32}°F"


# trouver_doublons(liste): retourne une liste des éléments qui apparaissent plus d'une fois dans la liste d'entrée. 
# Par exemple, pour la liste [1, 2, 2, 3, 3], le résultat serait [2, 3].

def trouver_doublons(liste):

  if not liste:
    raise ValueError("La liste est vide.")
  
  valeurs_uniques = []
  doublons = []

  for element in liste:
    if element in valeurs_uniques:
      if element not in doublons:
        doublons.append(element)
    else:
      valeurs_uniques.append(element)
  return doublons


# calculer_moyenne_ponderee(valeurs, poids): 
# calcule la moyenne pondérée d'une liste de valeurs avec une liste de poids correspondante et retourne un nombre. 
# Par exemple, pour les valeurs [3, 5] et les poids [1, 2], le résultat serait 4.33.

def calculer_moyenne_ponderee(valeurs, poids):

  total_valeurs = 0

  for index in range(len(valeurs)):
    total_valeurs += valeurs[index] * poids[index]

  moyenne_ponderee = total_valeurs / sum(poids)
  return moyenne_ponderee


# other way to do it:

def calculer_moy_ponderee(valeurs, poids):

  total_valeurs = 0

  for valeur, p in zip(valeurs, poids):
    total_valeurs += valeur * p

  return total_valeurs / sum(poids)
  
valeurs = [30, 50]
poids = [1, 2]

print(calculer_moy_ponderee(valeurs, poids))