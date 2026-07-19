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

