"""
Le programme suivant illustre cela dans le cas d'une boucle de répétition placé à l'intérieur d'un if. 
Ce programme lit un entier nommé cible. Si cible est un nombre positif, le programme affiche tous les entiers compris entre 1 et cible à l'aide d'une boucle de répétition. 
Sinon, le programme affiche le texte « Rien à faire ».
"""

# target = int(input())

# if target >= 0:
#   for number in range(target + 1):
#     print(number)
# else:
#   print("Rien à faire")


"""
Au cours de votre périple, vous traversez de nombreux lieux habités. 
Pour chacun d'entre eux, vous notez soigneusement sa population. 
Après quelques semaines de voyage, vous avez vraiment l'impression qu'il y beaucoup de villages et très peu de villes.

Ce que doit faire votre programme :
On vous donne le nombre d'habitants d'un certain nombre de lieux que vous visitez. 
Une ville étant un lieu dont la population est strictement supérieure à 10 000 habitants, déterminez combien de lieux sont des villes.

Votre programme doit lire un entier : le nombre de lieux. 
Il doit ensuite lire, pour chaque lieu, un entier donnant le nombre de gens qui y habitent. Votre programme doit alors afficher le nombre de villes.

Exemple
entrée :

6
1000
5000
15000
4780
0
23590
sortie :

2

"""

# places_number = int(input())
# number_of_cities = 0

# for place in range(places_number):
#   population = int(input())
#   if population > 10000:
#     number_of_cities += 1

# print(number_of_cities) 


"""
Vous venez d'arriver au bord d'un grand lac que vous devez contourner, par un côté ou l'autre, peu importe. Vous avez réussi à trouver une carte décrivant la position exacte de tous les villages le long de la route qui longe la rive du lac. 
Sachant que vous pouvez marcher 50 km dans la journée, vous aimeriez savoir dans combien de villages différents vous pourriez dormir la nuit prochaine.

Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier décrivant votre position actuelle sur la route, sous la forme d'un nombre de kilomètres par rapport au début de la route. 
Ensuite, il doit lire un entier donnant le nombre de villages. 
Pour chaque village, il doit lire un entier décrivant la position de ce village le long de cette même route. Votre programme doit alors afficher le nombre de villages qui se trouvent à une distance inférieure ou égale à 50 km de votre position actuelle.

Exemple
entrée :

120
5
30
113
187
145
129
sortie :

3
Commentaires
Vous êtes à la position 120 et il y a donc trois villages à moins de 50 km : ceux aux positions 113, 145 et 129. 
Les deux autres villages sont trop lointains.


"""

# current_position = int(input())
# villages_number = int(input())
# nearby_villages_count = 0

# for village in range(villages_number):
#   village_position = int(input())
#   if current_position -50 <= village_position <= current_position + 50:
#     nearby_villages_count += 1

# print (nearby_villages_count)
 

"""
Dans votre petit carnet de voyage, vous avez noté la distance que vous avez parcourue chaque jour. 
Aujourd'hui, vous êtes particulièrement en forme et vous décidez donc de marcher plus que les jours précédents. 
Vous souhaitez utiliser un programme pour déterminer quel est votre record pour l'instant.

Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier strictement positif, le nombre de jours de marche effectués jusqu'à présent. 
Il doit ensuite lire, pour chaque jour, la distance parcourue ce jour-là. 
Il doit alors afficher la distance maximale parcourue en une journée.

Exemple
entrée :

6
36
14
38
28
29
31
sortie :

38

"""

# days_number = int(input())
# distances = []

# for _ in range(days_number):
#   distance_day = int(input())
#   distances.append(distance_day)

# max_distance = max(distances)

# print(max_distance)

# other way to do it:

days_number = int(input())
max_distance = 0

for _ in range(days_number):
  distance_day = int(input())
  if distance_day > max_distance:
    max_distance = distance_day

print(max_distance)