"""
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

# distance_in_leagues = float(input())
# km_per_league = 1 / 0.707
# distance_in_km = distance_in_leagues * km_per_league

# print(distance_in_km)

"""

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

# vegetables_number = int(input())

# for vegatable in range(vegetables_number):
#   weight = float(input())
#   age = float(input())
#   price = float(input())
#   price_per_kg = price / weight
#   print(price_per_kg)



"""
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

scores_number = int(input())

total_scores = 0

for score in range(scores_number):
  score = int(input())
  total_scores += score
  
average = total_scores/scores_number

print(average)