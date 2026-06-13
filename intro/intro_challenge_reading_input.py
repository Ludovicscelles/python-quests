""" 
Les villageois font pousser dans leurs champs carrés un étrange légume géant : le Moutab. Les anciens vous ont dit que, d'après leurs estimations, le rendement de cette année serait de 23 kg de Moutab par mètre carré de culture. Vous voudriez écrire un programme permettant aux villageois de prédire la quantité de légume qu'ils peuvent espérer récolter dans chacun de leurs champs.

Ce que doit faire votre programme :
Votre programme doit lire un entier, qui représente la longueur du côté d'un champ carré en mètres. Il doit ensuite afficher la masse que l'on pourra récolter de ce champ si l'on suppose que la production sera de 23 kg par mètre carré.

Exemple
entrée :

10
sortie :

2300
Commentaires
Dans l'exemple, l'entrée contient l'entier 10 : l'utilisateur du programme souhaite donc obtenir la masse produite par un champ de côté 10 m. Le champ a une aire de 10 × 10 = 100 m² : la masse totale qu'on peut récolter est donc 100 × 23 = 2 300.

Pour l'entrée 10, la sortie est donc 2300.

À vous d'écrire un programme qui fonctionne quelle que soit la longueur du champ donnée au programme.


Exemple : 
Lire des entiers
On dispose de paquets de friandises dans lesquels les bonbons sont répartis dans des sachets de même contenance. On souhaite écrire un programme calculant le nombre total de bonbons dans un paquet, à partir du nombre de sachets dans le paquet et du nombre de bonbons par sachet. En Python, on fera ainsi :

nbSachets = int(input())
contenanceSachets = int(input())
print(nbSachets * contenanceSachets)
La ligne :

nbSachets = int(input())
récupère le premier entier de l'entrée (qui correspond au nombre de sachets) et le stocke dans la variable nbSachets. Il en est de même avec la ligne suivante pour le nombre de biscuits par sachet.

Comme int signifie « entier » et input signifie « entrée », int(input()) permet de prendre un entier sur l'entrée.

"""

side_length = int(input())
area = side_length ** 2
mass_per_square_meter = 23
total_mass = area * mass_per_square_meter

print(total_mass)

"""
Une fois par an, tout habitant de plus de 15 ans doit effectuer une randonnée spirituelle, celle-ci pouvant durer plusieurs jours. La durée dépendra du temps nécessaire à chaque personne pour faire le bilan de l'année écoulée. Au cours de cette randonnée, la personne doit répéter encore et encore la même incantation, une fois par seconde. Vous vous demandez combien de fois au total l'incantation aura été répétée, selon la durée de la randonnée.

Ce que doit faire votre programme :
Votre programme devra lire un entier : le nombre de jours que dure la randonnée. Ensuite, il devra afficher le nombre de fois que l'incantation est répétée, sachant qu'elle est prononcée une fois par seconde pendant 16 heures par jour (les 8 autres heures, on dort !).

Exemple
entrée :

2
sortie :

115200
Commentaires
En 2 jours (le nombre donné en entrée), l'incantation sera répétée 115 200 fois.

Écrivez à présent un programme qui fonctionne pour n'importe quel nombre de jours.

"""

days_number = int(input())
total_seconds = 16 * 3600 * days_number
total_incantions = total_seconds

print(total_incantions)

"""

Earane, la doyenne du village, a souhaité apprendre à programmer afin de pouvoir ensuite transmettre ce savoir à ses nombreux petits-enfants. 
Cependant, en dépit des quelques cours que vous lui avez donnés, elle n'arrive pas à terminer son premier programme. 
Pouvez-vous l'aider à corriger ses erreurs ?

Ce que doit faire votre programme :
Votre programme doit être une version corrigée du programme ci-dessous, sachant qu'il vous faut changer le moins de choses possible.

âgeCadet = int(input())
âgeAîné = int(input())
différence = âgeAîné - âgeDuCadet
print(différence)

"""

âgeCadet = int(input())
âgeAîné = int(input())
différence = âgeAîné - âgeCadet
print(différence)


"""

Les élèves du village ayant très souvent des punitions, ils aimeraient pouvoir venir les imprimer facilement sans que vous soyez là à chaque fois. Il leur suffirait d'indiquer le nombre de lignes voulu et le robot imprimerait tout seul la punition !

Ce que doit faire votre programme :
Votre programme doit lire un entier, le nombre de lignes souhaité, et écrira autant de fois que demandé la phrase « Je dois suivre en cours ».

Exemple
entrée :

3
sortie :

Je dois suivre en cours
Je dois suivre en cours
Je dois suivre en cours
Commentaires
3 lignes de punition sont demandées : on affiche donc 3 lignes en sortie.



"""
phrase = "Je dois suivre en cours"
lines_number = int(input())

for _ in range(lines_number):
    print(phrase)


"""
Les habitants du village utilisent beaucoup de thermomètres différents : certains pour l'été, d'autres pour l'hiver, d'autres pour la température de l'eau, etc. Ce qui change d'un thermomètre à l'autre, ce sont les valeurs de la température minimale et de la température maximale lisibles sur la graduation. Les habitants aimeraient pouvoir imprimer facilement la graduation des températures possibles pour chaque thermomètre.

Ce que doit faire votre programme :
Étant données deux températures entières tempMin et tempMax, votre programme doit afficher toutes les températures comprises entre les deux, bornes incluses.

Exemple
entrée :

9
14
sortie :

9
10
11
12
13
14

"""

min_temp = int(input())
max_temp = int(input())

for temperature in range(min_temp, max_temp + 1):
    print(temperature)
    

