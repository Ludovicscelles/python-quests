"""
Origami

Des enfants découvrent les joies de l'origami (créer des objets en pliant une feuille de papier), et l'un d'eux s'amuse à replier sur elle-même une feuille le plus de fois possible. 
Il pense qu'il peut replier la feuille en deux 15 fois de suite !

Vous pressentez que cela risque fort d'être impossible. 
Pendant qu'il essaie, vous décidez de calculer l'épaisseur qu'aurait son pliage final si par hasard l'enfant arrivait à atteindre son objectif.

Ce que doit faire votre programme :
L'épaisseur d'une feuille de papier est de 110 micromètres c'est à dire 0,110 millimètres. 
Si on la plie 15 fois sur elle-même et que l'épaisseur double à chaque fois, quelle sera l'épaisseur finale si on l'exprime en centimètres ? 
Votre programme devra calculer et afficher cette valeur (qui n'est pas forcément entière).


"""

thickness_sheet = 0.11
folding_number = 15
final_thickness = thickness_sheet

for fold in range(15):
  final_thickness *= 2

print(final_thickness/10)

"""
Conversions des distances

Vous décidez de partir pour quelques jours de randonnée à la montagne. 
Le problème est que toutes les distances indiquées sur les panneaux ne le sont pas en kilomètres mais en lieues. 
Vous aimeriez être en mesure de faire les conversions automatiquement.

Ce que doit faire votre programme :
Écrivez un programme qui lit un nombre décimal (un nombre à virgule) représentant un nombre de lieues et affiche le nombre de kilomètres correspondant. 
Un kilomètre vaut exactement 0.707 lieues.

Exemple
entrée :

10.5
sortie :

14.8514851485


"""

distance_in_leagues = float(input())
km_per_league = 1 / 0.707
distance_in_km = distance_in_leagues * km_per_league

print(distance_in_km)

"""

Comparatif de prix

Lors du marché hebdomadaire, de nombreux maraîchers viennent vendre de très gros légumes, en indiquant pour chacun trois informations : son poids, le nombre de jours qui se sont écoulés depuis sa cueillette, et son prix.

Il n'est vraiment pas évident de comparer les prix de légumes de différentes tailles, et des habitants vous demandent de les aider à répondre à cette question. Vous décidez d'écrire un programme qui calcule le prix au kg de chaque légume à partir des informations disponibles.

Ce que doit faire votre programme :
Votre programme doit d'abord lire le nombre de légumes mis en vente. Ensuite, pour chacun, il doit lire 3 nombres décimaux : son poids, son âge (en nombre de jours depuis la cueillette), et son prix de vente. Votre programme doit ensuite afficher pour chaque légume son prix au kg (au fur et à mesure que les légumes sont présentés).

Exemple
entrée :

2
7.0
5.0
14.0
9.5
2.3
7.6
sortie :

2.0
0.8

"""

vegetables_number = int(input())

for vegatable in range(vegetables_number):
  weight = float(input())
  age = float(input())
  price = float(input())
  price_per_kg = price / weight
  print(price_per_kg)



"""

Moyenne de notes 

Des écoliers d'une école voisine aiment bien calculer la moyenne qu'ils vont avoir sur leur bulletin de notes avant de le recevoir. 
Cependant, ils ont beaucoup de notes, et ils aimeraient donc pouvoir utiliser un petit programme pour calculer leur moyenne sans se fatiguer.

Le nombre de notes dépend non seulement des matières, mais aussi des possibles absences de chacun. 
Aussi, le programme doit être capable de calculer la moyenne d'un nombre arbitraire de notes. 
C'est pourquoi vous concevez un programme auquel il faut d'abord fournir le nombre de notes dont il faut faire la moyenne, puis fournir les notes elles-mêmes (une par une).

Ce que doit faire votre programme :
Votre programme doit d'abord lire un premier entier, qui décrit le nombre de notes obtenues. 
Ensuite, il doit lire chacune de ces notes, qui sont également des nombres entiers. Enfin, il doit afficher la moyenne de toutes ces notes.

Exemple
entrée :

3
10
14
15
sortie :

13.0


"""

# scores_number = int(input())

# total_scores = 0

# for score in range(scores_number):
#   score = int(input())
#   total_scores += score
  
# average = total_scores/scores_number

# print(average)

# Précision des calculs

print(2/3)

# À l'affichage on obtient 0.6666666666666666, mais en réalité la valeur exacte de 2/3 est 0.66666... à l'infini.

print(1.0 - 0.000000000000000000000001)

# À l'affichage on obtient 1.0, mais en réalité la valeur exacte de 1.0 - 0.000000000000000000000001 est 0.999999999999999999999999, c'est à dire légèrement inférieure à 1.0.

print(13212314656 * 1564651126454465213)

# À l'inverse, des nombres entiers ne sont jamais arrondis, et ici on obtient donc le résultat exact de 20635809118715584000000000.

big_number = 1000 * 1000 * 1000 * 1000 * 1000 * 1000

number = big_number + 1
print(number)


number = (big_number + 1) / 1
print(number) # On obtient 1000000000000000000.0, c'est à dire 1.0 * 10^18, ce qui est bien le résultat attendu.

number = (big_number + 1) / 1 - big_number # On obtient 0.0, alors que le résultat attendu est 1.0. 
                                          # Cela est dû au fait que le calcul a été effectué avec des nombres flottants, et que la précision de ces nombres est limitée.


print(12345678987654321 * 1234567.89)

# Faire des arrondis (inférieurs ou supérieurs) avec les fonctions floor() et ceil() du module math.

from math import *

# Entier inférieur (partie entière) d'un nombre décimal

arrondi_inf = floor(12.3)
print(arrondi_inf) # Affiche 12

# Entier supérieur d'un nombre décimal
arrondi_sup = ceil(12.3)
print(arrondi_sup) # Affiche 13

# Attention si le nombre est négatif !

# Entier inférieur (partie entière) d'un nombre décimal négatif
arrondi_inf_negatif = floor(-12.3)
print(arrondi_inf_negatif) # Affiche -13

# Entier supérieur d'un nombre décimal négatif
arrondi_sup_negatif = ceil(-12.3)
print(arrondi_sup_negatif) # Affiche -12

""""
Augmentation de la population

Ces dernières années, la population de votre ville a très fortement augmenté, grâce à un fort taux de natalité. Cela pose cependant un certain nombre de problèmes, notamment une pénurie de logements ! Le maire a décidé de s'occuper du problème et souhaiterait estimer l'évolution future de la population.

Ce que doit faire votre programme :
Votre programme devra lire un entier, la population actuelle de la ville, puis un nombre décimal, la croissance prévue de la population, en pourcentage. Il devra alors afficher la nouvelle population de la ville sous la forme d'un nombre entier. On considérera, par convention, qu'une population de 31,4 habitants signifie qu'il y a 31 habitants, on ne compte donc que les habitants « entiers » !

Exemples
Exemple 1
entrée :

123
7.0
sortie :

131
Exemple 2
entrée :

456
-5.5
sortie :

430



"""
from math import *

population = int(input())

growth = float(input())

new_population = floor(population * (1 + growth/100))

print(new_population)


"""
Construction de maisons 

Pour la construction de votre nouvelle maison, vous avez calculé la quantité de ciment nécessaire pour construire les fondations. De nature économe, vous souhaitez acheter exactement la quantité nécessaire mais malheureusement le magasin ne vend le ciment qu'en gros sacs. Vous souhaitez calculer combien tout cela va vous coûter.

Ce que doit faire votre programme :
Votre programme devra lire un nombre décimal, la quantité de ciment nécessaire pour les fondations de votre nouvelle maison, en kilos. Sachant que le ciment n'est vendu qu'en sacs de 60 kilos et que un sac coûte 45 euros, votre programme devra afficher le coût total du ciment.

Exemple
entrée :

145.8
sortie :

135


"""

from math import *

amount_of_ciment = float(input())

BAG_WEIGHT = 60

BAG_PRICE = 45

number_of_bags = ceil(amount_of_ciment / BAG_WEIGHT)

total_price = BAG_PRICE * number_of_bags

print(total_price)



# Faire des arrondis au plus proche 

# Utilisation de round() pour arrondir un nombre décimal au plus proche entier.

arrondi_pro = round(12.3)
print(arrondi_pro) # Affiche 12

arrondi_per_def = round(12.5)
print(arrondi_per_def) # Affiche 12, car par défaut, round() arrondit au plus proche entier pair.

arrondi_per_def = round(13.5)
print(arrondi_per_def) # Affiche 14, car par défaut, round() arrondit au plus proche entier pair.

# arrondir à l'entier inférieur le plus proche
arrondi_inf_per_def = round(12.5 - 0.5)
print(arrondi_inf_per_def) # Affiche 12, car par défaut, round() arrondit au plus proche entier pair.

# arrondir à l'entier supérieur le plus proche
arrondi_sup_pro = round(12.3 + 0.5)
print(arrondi_sup_pro) # Affiche 13

# arrodir vers zéro
arrondi_vers_zero = round(-12.3 + 0.5)
print(arrondi_vers_zero) # Affiche -12

# arrondir vers l'infini
arrondi_vers_inf = round(-12.3 - 0.5)
print(arrondi_vers_inf) # Affiche -13

# arrondissement bancaire (ou arrondi statistique) : arrondir à l'entier pair le plus proche si la partie décimale est exactement 0.5, sinon arrondir au plus proche entier.

arrondi_bancaire = round(12.5)
print(arrondi_bancaire) # Affiche 12, car 12 est pair.

arrondi_bancaire = round(13.5)
print(arrondi_bancaire) # Affiche 14, car 14 est pair.

arrondi_bancaire = round(12.3)
print(arrondi_bancaire) # Affiche 12, car 12 est le plus proche entier.

print(round(-1.5)); print(round(-0.5)); print(round(0.5)); print(round(1.5))

"""
Soirée orageuse 

Ce soir, un orage se déchaîne pas loin de chez vous et régulièrement vous voyez des éclairs puis, quelques secondes après, vous entendez le tonnerre. Vous aimeriez savoir à quelle distance se trouve l'orage, afin de savoir s'il se rapproche de vous ou, au contraire, s'éloigne.

Ce que doit faire votre programme :
Votre programme devra lire un décimal, le temps (en secondes) entre le moment où vous voyez l'éclair et le moment où vous entendez le tonnerre. Il devra calculer et afficher la distance entre vous et l'orage, arrondi au kilomètre près.

On supposera que la lumière se déplace instantanément. La vitesse du son dépend de paramètres comme l'altitude, la température...mais on supposera qu'en cette soirée elle vaut 340,29 mètres / seconde.

Exemple
entrée :

3.0
sortie :

1

"""

time_in_s = float(input())
sound_velocity = 340.29
distance_in_km = round((time_in_s * sound_velocity) / 1000)

print(distance_in_km)

"""
Augmentation des taxes

Pour faire face à des difficultés financières du gouvernement, la taxe sur les fruits et légumes a été augmentée. Il faut donc recalculer tous les prix afin de prendre en compte cette nouvelle taxe, que les commerçants vont bien entendu répercuter sur les clients.

Ce que doit faire votre programme :
Votre programme doit lire trois nombres décimaux : la valeur actuelle de la taxe sur les fruits et légumes (en pourcentage), la nouvelle valeur de la taxe (en pourcentage), puis le prix actuel d'un légume, taxes comprises, en euros. Il devra calculer et afficher le prix du légume avec la nouvelle valeur de la taxe, arrondi au centime près.

Exemples
Exemple 1
entrée :

5.5
19.6
24.9
sortie :

28.23
Exemple 2
entrée :

21.5
21.5
19.99
sortie :

19.99
Commentaires
On rappelle qu'une taxe de 15% signifie que pour un prix hors-taxe de 100 euros, le prix avec taxe sera de 115 euros.



"""

current_tax = float(input())
new_tax = float(input())
current_price = float(input())

current_price_without_vat = current_price / (1 + current_tax/100)

new_price = round(current_price_without_vat * (1 + new_tax/100), 2)

print(new_price)


# Division entière et reste

# En Python, il est possible de calculer le quotient et le reste d'une division entière avec les opérateurs // et %.

nb_boites = 666 // 13
nb_reste = 666 % 13
print(nb_boites) # Affiche 51
print(nb_reste) # Affiche 3

# Si dividende negatif, le quotient est arrondi à l'entier inférieur (vers -infini) et le reste est toujours positif.

print(-666 // 50) # Affiche -14
print(-666 % 50) # Affiche 34

""""
Achat de livres 

ous commencez à apprendre une nouvelle langue et décidez d'acheter quelques livres pour vous entraîner. 
Vous trouvez un vendeur qui propose de nombreux livres à des prix avantageux. Vous disposez d'une certaine somme d'argent et vous vous demandez combien de livres vous pouvez acheter, sachant qu'ils sont tous au même prix.

Ce que doit faire votre programme :
Votre programme doit commencer par lire la somme d'argent dont vous disposez et lira ensuite le prix d'un livre. 
Il devra ensuite afficher un entier, le plus grand nombre de livres qu'il vous est possible d'acheter avec cette somme d'argent.

Exemple
entrée :

27
5
sortie :

5


"""

money = int(input())
book_price = int(input())

max_books = money // book_price

print(max_books)

"""

Une belle récolte


Vous êtes chargé d'acheter des fruits pour un grand repas organisé pour fêter la dernière récolte qui a été très fructueuse. Les vendeurs proposent généralement leurs fruits par paquets. Vous souhaitez acheter un paquet dont le nombre de fruits soit un multiple du nombre de personnes conviées, de sorte que chaque invité ait le même nombre de fruits.

Ce que doit faire votre programme :
Votre programme doit commencer par lire un entier nbPersonnes puis un entier nbFruits. Il doit ensuite afficher "oui" si nbFruits est un multiple de nbPersonnes, et "non" dans le cas contraire.

Exemple
entrée :

12
156
sortie :

oui

"""

guests_number = int(input())

fruits_number = int(input())

if fruits_number % guests_number == 0:
  print("oui")
else:
  print("non")


# Priorité des opérateurs division entière et reste

# En Python, la priorité des opérateurs est la suivante : les opérateurs de multiplication, division et reste ont la même priorité, et sont évalués de gauche à droite.
# Ainsi, l'expression 10 // 3 * 2 est évaluée comme suit : (10 // 3) * 2 = 3 * 2 = 6.
# L'expression 10 % 3 * 2 est évaluée comme suit : (10 % 3) * 2 = 1 * 2 = 2.

# Cas complexes:

print(100 * 200 // 300 // 40 % 50) # Affiche 1, car l'expression est évaluée comme suit : (((100 * 200) // 300) // 40) % 50 = (20000 // 300 // 40) % 50 = (66 // 40) % 50 = 1 % 50 = 1.

# Pour ce cas, il faut faire du parenthésage pour comprendre l'ordre d'évaluation des opérations.

# exemples:

print(100 * (200 // (300 // (40 % 50)))) # Affiche 2800
print((((100 * 200) // 300) // 40) % 50) # Affiche 1


"""
La roue de la fortune

Lors de l'examen final à la fin de leurs études, la tradition veut que les élèves tirent un sujet au hasard. 
Tirer un numéro dans un chapeau n'étant pas très amusant, ils utilisent une roue comme celle-ci, qu'ils peuvent faire tourner dans un sens ou dans l'autre.

Les enseignants, par expérience, arrivent toujours à estimer de combien de "zones" la roue va tourner et peuvent aller chercher le sujet et revenir, pendant que la roue tourne encore. 
Il faut, pour cela, calculer rapidement sur quelle zone le curseur va s'arrêter, en fonction du nombre de zones dont la roue va tourner. A vous de jouer !

Ce que doit faire votre programme :
Votre programme doit commencer par lire un entier nbZones. 
Sachant que la roue va tourner de nbZones zones, vous devez calculer (puis afficher) sur quelle zone le curseur va arriver.

Ainsi, si la route tourne de +2 zones alors le curseur arrive sur la zone 2, et si la roue tourne de -2 zones, alors le curseur arrive sur la zone 22.

Exemples
Exemple 1
entrée :

25
sortie :

1
Exemple 2
entrée :

-50
sortie :

22


"""

zones_nb = int(input())
entire_tour = 24


arrival_zone = zones_nb % entire_tour

print(arrival_zone)

