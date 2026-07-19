# Variables

PI = 3.14159
E = 2.71828

# Functions

def carre(x):
  return x ** 2

def cube(x):
  return x ** 3

def factorielle(x):
  if x < 0:
    raise ValueError("Il est impossible de définir la factorielle d'un nombre négatif.")
  
  result = 1
  if x == 0 or x == 1:
    return result
  else:
    for i in range(2, x + 1):
      result *= i
    return result
  
def valeur_absolue(x):
  if x < 0:
    return -x
  else:
    return x
  
def maximum(liste):

  if not liste:
    raise ValueError("La liste est vide.")
    
  maximum_num = liste[0]

  for i in liste:
    if i > maximum_num:
      maximum_num = i
    
  return maximum_num

def minimum(liste):

  if not liste:
    raise ValueError("La liste est vide.")

  minimum_num = liste[0]

  for i in liste:
    if i < minimum_num:
      minimum_num = i
  
  return minimum_num

def moyenne(liste):

  if not liste:
    raise ValueError("La liste est vide.")

  total = 0

  for i in liste:
    total += i

  moy = total/len(liste)
  return moy

def ecart_type(liste):
  
  if not liste:
    raise ValueError("La liste est vide.")
  
  valeur_moyenne = moyenne(liste)

  somme = 0

  for x in liste:
    # somme = somme des carrés des écarts à la moyenne
    somme += (x - valeur_moyenne) ** 2

  # variance = moyenne des carrés des écarts à la moyenne
  variance = somme / len(liste)

  # écart-type = racine carrée de la variance
  return variance ** 0.5

def mediane(liste):

  if not liste:
    raise ValueError("La liste est vide.")
  
  nombres_tries = sorted(liste)
  nombres_valeurs = len(nombres_tries)
  milieu = nombres_valeurs // 2

  if nombres_valeurs % 2 == 0:
    return(nombres_tries[milieu - 1] + nombres_tries[milieu])/ 2
  else:
    return nombres_tries[milieu]
