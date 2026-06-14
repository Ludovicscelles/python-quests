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

# side_length = int(input())
# area = side_length ** 2
# mass_per_square_meter = 23
# total_mass = area * mass_per_square_meter

# print(total_mass)

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

# days_number = int(input())
# total_seconds = 16 * 3600 * days_number
# total_incantions = total_seconds

# print(total_incantions)

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

# âgeCadet = int(input())
# âgeAîné = int(input())
# différence = âgeAîné - âgeCadet
# print(différence)


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
# phrase = "Je dois suivre en cours"
# lines_number = int(input())

# for _ in range(lines_number):
#     print(phrase)


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

# min_temp = int(input())
# max_temp = int(input())

# for temperature in range(min_temp, max_temp + 1):
#     print(temperature)
    


"""
Au village, la passion pour le calcul mental est une tradition : des jeux centrés sur cette pratique sont régulièrement organisés par les habitants. Pour chaque jeu, ils décident d'abord combien de nombres devront être prononcés ; puis chaque joueur doit effectuer un calcul déterminé par les règles du jeu. Chaque fois que quelqu'un se trompe et qu'un autre joueur s'en rend compte, le joueur qui s'est trompé doit se corriger, et il devra un Gombo (une friandise du coin) à celui qui lui a signalé son erreur le plus rapidement.

Vous aimeriez participer, mais les habitants vont si vite et manipulent des nombres si grands que vous êtes tout de suite dépassé par les calculs ! Alors qu'un nouveau jeu se prépare, vous décidez finalement d'utiliser votre robot pour vous aider à rivaliser.

Ce que doit faire votre programme :
Un nombre de départ va être donné par le chef du village. La personne qui suit doit le multiplier par 2, puis la suivante doit multiplier le nombre obtenu par 3, celle d'encore après doit multiplier le résultat par 4… jusqu'à ce que les nbNombres calculs aient été effectués.

Le chef a choisi le nombre 66 pour démarrer le jeu. Votre programme lira l'entier nbNombres, la quantité de nombres attendue par le jeu (nombre de départ inclus). Il devra ensuite afficher tous les nombres de la partie afin de vous rendre imbattable !

Exemples
Exemple 1
entrée :

4
sortie :

66
132
396
1584
Exemple 2
entrée :

1
sortie :

66
Commentaires
Les valeurs du premier exemple correspondent aux calculs suivants :

66
66 × 2 = 132
132 × 3 = 396
396 × 4 = 1584


"""

# number_of_inputs = int(input())
# depart_number = 66

# result = depart_number

# for i in range(1, number_of_inputs + 1):
#     result *= i
#     print(result)


""""

Chaque année, c'est la tradition, une grande braderie est organisée dans le village et toute la région y participe. 
C'est l'occasion pour les habitants de vendre quelques petits objets qui traînent dans le grenier depuis des années. 
Afin que cela soit équitable, chaque vendeur doit avoir à sa disposition la même longueur de rue pour installer ses affaires. 
Pour délimiter les emplacements, des marques sont faites à la peinture à intervalles réguliers. 
Les villageois vous demandent votre aide pour calculer les positions (c'est-à-dire la distance par rapport au début de la rue) auxquelles ces marques doivent être faites.


Ce que doit faire votre programme :
Il y a trois entiers à lire : la position de départ positionDepart, la largeur d'un emplacement largeurEmplacement et le nombre de vendeurs nbVendeurs.

Vous devez afficher une suite de nombres, partant de positionDepart et augmentant de largeurEmplacement à chaque fois. 
Il y a au total nbVendeurs augmentations à faire. 
Vous devez afficher la valeur de chacun des nombres de la suite.

Exemples
Exemple 1
entrée :

10
5
3
sortie :

10
15
20
25
Exemple 2
entrée :

12
8
5
sortie :

12
20
28
36
44
52



"""

# depart_position = int(input())
# slot_width = int(input())
# number_of_sellers = int(input())

# position = depart_position

# print(position)

# for _ in range(number_of_sellers):
#   position += slot_width
#   print(position)

# Other way to do it

# depart_position = int(input())
# slot_width = int(input())
# number_of_sellers = int(input())

# for i in range(number_of_sellers +1):
#   position = depart_position + i * slot_width
#   print(position)


"""
Le village compte 20 fermiers, et chaque fermier élève un certain nombre de Karvas (des ruminants qui ressemblent beaucoup à nos vaches terriennes). 
Pour s'assurer qu'il n'y a pas de risque de famine en cas de mauvaise récolte, les habitants veulent régulièrement calculer le nombre total de Karvas du village. 
Cependant, pour une raison qui vous échappe, les fermiers gardent jalousement secret le nombre de bêtes qu'ils possèdent.

Vous proposez alors la solution suivante : les fermiers viendront chacun leur tour donner à votre robot le nombre de Karvas qu'ils possèdent. 
Votre robot pourra alors afficher le nombre total de Karvas du village, puis effacer les informations secrètes qui lui auront été fournies.

Ce que doit faire votre programme :
Votre programme doit lire 20 entiers puis afficher la somme de tous ces entiers.

Exemples
Exemple 1
entrée :

entrée :

1
2
3
4
5
6
7
8
9
10
10
9
8
7
6
5
4
3
2
1
sortie :

110
Exemple 2
entrée :

1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
sortie :

30

"""

# farmers_number = 20
# karvas_farmers_list = []

# for _ in range(farmers_number):
#   karvas_per_farmer = int(input())
#   karvas_farmers_list.append(karvas_per_farmer)

# total_karvas = sum(karvas_farmers_list)

# print(total_karvas)

""""
Les habitants d'Algoréa aiment bien ériger des statues et les poser sur des socles majestueux. 
Selon les dimensions de la statue, le socle doit être plus ou moins haut et offrir une surface plus ou moins grande pour y poser la statue. 
Cependant, les constructeurs de statues ont souvent du mal à estimer la quantité de béton nécessaire à la construction de chaque socle. 
Vous souhaitez écrire un programme pour les aider.

Ce que doit faire votre programme :
Voici un exemple de socle :

Pyramide formée de 3 marches carrées de tailles décroissantes
Un socle est ainsi constitué d'étages, chaque étage ayant une hauteur égale à une unité et une base carrée. 
Le côté des carrés diminue de une unité à chaque étage.

Votre programme doit lire deux entiers, représentant respectivement la largeur du socle au niveau du sol et la largeur du socle au niveau de la face supérieure du socle. 
Il doit ensuite calculer et afficher le volume du socle.

Exemple
entrée :

7
3
sortie :

135
Commentaires
Le volume du premier étage est 7 × 7 = 49, le volume du second est 6 × 6 = 36, etc. et le volume du dernier étage est 3 × 3 = 9. 
Le volume total est donc : 7 × 7 + 6 × 6 + 5 × 5 + 4 × 4 + 3 × 3 = 135.

"""

# base_floor_width = int(input())
# base_top_face_width = int(input())

# total_volume = 0

# for i in range(base_top_face_width, base_floor_width + 1):
#   total_volume += (i ** 2)

# print(total_volume)


""""
Lors du concours général agricole, l'épreuve reine, celle que tout fermier rêve de remporter, est celle du plus beau Karva (l'équivalent de notre taureau). La compétition est basée sur des règles strictes : chaque animal reçoit une note en fonction de ses caractéristiques et celui qui a reçu la plus grande note est déclaré champion. Vous souhaiteriez connaître les résultats avant tout le monde ; aussi, vous décidez d'écrire un programme qui vous donnera la note de chacun des Karvas en compétition.

Ce que doit faire votre programme :
Votre programme doit d'abord lire le nombre de Karvas en compétition. Ensuite, pour chaque Karva, il doit :

lire 4 entiers : son poids, son âge, la longueur de ses cornes et la hauteur au garrot ;
afficher sa note, sachant qu'elle s'obtient en multipliant la longueur des cornes par la hauteur au garrot, valeur à laquelle on ajoute le poids.
Exemple
entrée :

2
100
5
25
90
300
10
15
120
sortie :

2350
2100

"""


karva_number = int(input())
karva_scores = []

for karva in range(karva_number):
  weight_karva = int(input())
  age_karva = int(input())
  horns_length_karva = int(input())
  garot_height_karva = int(input())
  karva_score = horns_length_karva * garot_height_karva + weight_karva
  karva_scores.append(karva_score)

for score in karva_scores:
  print(score)



