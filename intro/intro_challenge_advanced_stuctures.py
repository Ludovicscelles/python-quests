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

# days_number = int(input())
# max_distance = 0

# for _ in range(days_number):
#   distance_day = int(input())
#   if distance_day > max_distance:
#     max_distance = distance_day

# print(max_distance)

"""

Calcul des dénivelées

Aujourd'hui c'est l'étape de montagne et vous allez devoir franchir plusieurs cols. 
Vous allez passer votre temps à monter, descendre, remonter, redescendre, etc... 
Vous décidez de noter les différentes variations d'altitudes, afin de pouvoir calculer à la fin de la journée quelle est la dénivelée totale que vous avez montée ainsi que la dénivelée totale que vous avez descendue 
(les deux valeurs peuvent être différentes car vous ne retournez pas à votre point de départ).

Ce que doit faire votre programme :
Votre programme lira d'abord un entier représentant le nombre de montées et descentes que vous avez réalisées. 
Pour chaque montée ou descente, il faut ensuite lire un entier représentant la variation d'altitude, cet entier étant strictement positif dans le cas d'une montée et strictement négatif dans le cas d'une descente (il n'y a rien à compter pour les tronçons qui sont bien à plat). 
Votre programme devra afficher l'altitude totale montée puis l'altitude totale descendue (ces deux nombres sont positifs).

Exemple
entrée :

5
4
7
-6
-3
2
sortie :

13
9

"""

# number_of_slopes = int(input())
# total_ascents = 0
# total_descents = 0

# for _ in range(number_of_slopes):
#   slopes = int(input())
#   if slopes < 0:
#     total_descents += abs(slopes)
#   else:
#     total_ascents += slopes

# print(total_ascents)
# print(total_descents)

""""
Alors que vous traversez une forêt vous ne pouvez vous empêcher d'admirer la végétation autour de vous et notamment les nombreuses espèces d'arbres. 
Malgré votre intérêt, vous êtes très mauvais botaniste et avez beaucoup de mal à identifier les différents arbres. 
Une personne que vous croisez vous donne quelques indications et vous décidez d'écrire un programme qui vous donnera le nom de l'arbre en fonction de ses caractéristiques.

Ce que doit faire votre programme :
Il existe 4 types d'arbres :

le "Tinuviel" fait moins de 5 mètres de haut et ses feuilles sont composées de plus de 8 folioles
le "Calaelen" fait plus de 10 mètres de haut et ses feuilles sont composées de plus 10 folioles
le "Falarion" fait moins de 8 mètres de haut et ses feuilles sont composées de moins de 5 folioles
le "Dorthonion" fait plus de 12 mètres de haut et ses feuilles sont composées de moins de 7 folioles
Votre programme lira deux entiers, la hauteur et le nombre de folioles de l'arbre, et affichera le nom de l'arbre correspondant.
Toutes les inégalités sont à prendre au sens large, c'est-à-dire que "moins" signifie "moins ou égal" ou et "plus" signifie "plus ou égal".

Exemples
Exemple 1
entrée :

12
12
sortie :

Calaelen
Exemple 2
entrée :

4
9
sortie :

Tinuviel


"""

# height = int(input())
# leaflets = int(input())

# if height <= 5 and leaflets >= 8:
#   print("Tinuviel")
# elif height <= 8 and leaflets <= 5:
#   print("Falarion")
# elif height >= 10 and leaflets >= 10:
#   print("Calaelen")
# elif height >= 12 and leaflets <= 7:
#   print("Dorthonion")
# else:
#   print("Espèce inconnue")


""""
L'auberge dans laquelle vous vous arrêtez pour la nuit adapte ses prix en fonction de l'âge du client et du poids de ses bagages. 
Les règles ne vous étant pas très claires, vous décidez d'écrire un petit programme qui vous permettra facilement, à vous et à vos compagnons de voyage, de connaître le prix d'une nuit.

Ce que doit faire votre programme :
Une chambre ne coûte rien si on a 60 ans (l'âge de l'aubergiste !) et 5 écus si on a strictement moins de 10 ans. 
Pour les autres personnes c'est 30 écus plus un supplément de 10 écus si on a au moins 20 kilos de bagages.

Votre programme doit lire deux entiers, l'âge et le poids des bagages de la personne et doit afficher le prix, sous la forme d'un entier.

Exemple
entrée :

22
25
sortie :

40


"""

# age = int(input())
# luggage_weight = int(input())
# bedroom_price = 0

# if age == 60:
#   bedroom_price += 0
# elif age < 10:
#   bedroom_price += 5
# else: 
#   bedroom_price += 30
#   if luggage_weight >= 20:
#     bedroom_price += 10

# print(bedroom_price)


""""

Le village dans lequel vous avez passé la nuit est en pleine effervescence au matin : encore une attaque de worgs pendant la nuit ! 
Les worgs sont de redoutables loups qui vivent sur Algoréa et qui s'attaquent au bétail... et parfois même aux enfants.

C'est décidé, il va falloir construire une grande palissade tout autour du village. 
Les habitants insistent pour que cette clôture soit rectangulaire et ait une face au Nord, une au Sud, une à l'Est et une à l'Ouest, quitte à devoir travailler un peu plus que nécessaire. 
Ils ont maintenant besoin de votre aide pour savoir la quantité de bois dont ils vont avoir besoin pour construire cette palissade.

Ce que doit faire votre programme :
Le programme doit d'abord lire un entier strictement positif correspondant au nombre de maisons. 
Ensuite, pour chaque maison, il doit lire la position horizontale (l'abscisse, le "x") et sa position verticale (l'ordonnée, le "y") de cette maison. 
Toutes les abscisses et ordonnées sont des entiers compris entre zéro et 1 million.

Le programme doit alors afficher le périmètre de la plus petite clôture rectangulaire englobant toutes les maisons. 
Ce rectangle doit avoir ses côtés parallèles aux axes du repère, comme montré sur l'illustration.

"""

# houses_number = int(input())
# x_list = []
# y_list = []

# for house in range(houses_number):
#   axis_x = int(input())
#   x_list.append(axis_x)
#   axis_y = int(input())
#   y_list.append(axis_y)
  
# area = ((max(x_list) - min(x_list)) + (max(y_list) - min(y_list))) * 2

# print(area)


""""
Vous arrivez dans un village le jour du marché, de nombreux marchands vendent la spécialité locale, de délicieuses petites galettes. 
Elles ont toutes l'air d'être identiques, donc vous décidez d'acheter les moins chères.

Ce que doit faire votre programme :
Votre programme doit lire un entier nbMarchands (non nul) puis les nbMarchands entiers suivants, qui indiquent le prix des galettes chez chaque marchand, de la position 1 à la position nbMarchands. 
Votre programme devra ensuite afficher la position du plus petit de ces prix. En cas d'égalité entre deux prix, on prendra la position la plus grande. 
Tous les prix et positions sont positifs et ne dépassent pas 1 million.

Exemple
entrée :

6
12
11
9
11
9
15
sortie :

5
Commentaires
Parmi ces 6 marchands, c'est le 5ème qui vend ses galettes le moins cher, à 9 euros la galette. 
Il est à égalité avec le 3e marchand, mais on préfère le 5e qui est le plus près du bout de la rue.




"""

# merchants_number = int(input())
# galettes_prices = []
# best_merchant = 1

# for merchant in range (merchants_number):
#   galette_price = int(input())
#   galettes_prices.append(galette_price)
#   if galette_price < min(galettes_prices):
#     best_merchant = galettes_prices[best_merchant]

# min_galette_price = min(galettes_prices)


merchants_number = int(input())

min_price_galette = int(input())
best_merchant_position = 1

for merchant in range (2, merchants_number + 1):
  price_galette = int(input())

  if price_galette < min_price_galette:
    min_price_galette = price_galette
    best_merchant_position = merchant
  
  elif price_galette == min_price_galette:
    best_merchant_position = merchant

print(best_merchant_position)


