"""
Alors que vous quittez le village, les villageois vous offrent de nombreux cadeaux : provisions, vêtements chauds, boissons… Vous ne pourrez jamais porter tout cela tout seul ; vous décidez donc de donner une partie de ces objets à votre robot, après les avoir rassemblés en de gros paquets, tous de même masse. Aura-t-il la force de tout porter ?

Ce que doit faire votre programme :
Votre programme lira deux entiers : le nombre de paquets et le poids d'un paquet. Si le poids total est strictement supérieur à 105 kg, votre programme devra alors afficher le texte « Surcharge ! ».

Exemples
Exemple 1
entrée :

10
15
sortie :

Surcharge !
Exemple 2
entrée :

3
7
sortie :



Conditionner une action
La célèbre attraction du train fou est interdite aux moins de 10 ans. On souhaite écrire un programme qui demande à l'utilisateur son âge et qui, si la personne a moins de 10 ans, affiche le texte « Accès interdit » ; ce qui peut se rédiger comme cela :

âge <- lireEntier()
Si âge < 10
   Afficher "Accès interdit"
Voyons comment cela se traduit en Python :

âge = int(input())
if âge < 10:
   print("Accès interdit")
On écrit donc le mot-clef if, la traduction en anglais de « si », la condition à tester, à savoir âge < 10, puis on termine la ligne avec un deux-points, comme on le faisait pour la boucle de répétition.

Ainsi, l'accès est interdit à un enfant de 8 ans :

↳
8
↳
Accès interdit
À l'opposé, le programme n'affiche rien pour un âge de 13 ans :

↳
13 
↳
 
Pour exprimer la condition du « si » dans le programme, on a utilisé le symbole <, qui est l'opérateur de comparaison strictement inférieur. De manière symétrique, l'opérateur > permet de tester si un nombre est strictement supérieur à un autre.

Lorsqu'on veut tester si un nombre est inférieur ou égal à un autre, on utilise le symbole <=. De manière symétrique, le symbole >= permet de tester si un nombre est supérieur ou égal à un autre.

Par exemple, le code suivant permet de tester si la température de l'eau a atteint 100 degrés.

température = int(input())
if température >= 100:
   print("L'eau bout !")


"""

packages_number = int(input())
weight_of_a_package = int(input())
total_weight = packages_number * weight_of_a_package
alert = str("Surcharge !")

if total_weight > 105:
   print(alert)


""""
Le long de la route sur laquelle vous marchez se trouvent des bornes. Sur chaque borne est écrit le nombre de kilomètres séparant la position actuelle du bout de la route. Si la borne numéro zéro se trouve derrière vous, alors les numéros augmentent au fur et à mesure que vous avancez. Au contraire, si la borne zéro se trouve devant vous, alors les numéros diminuent au fur et à mesure que vous avancez.

Vous avez noté le numéro de la borne de laquelle vous êtes parti(e) ce matin, ainsi que le numéro de la borne à laquelle vous êtes arrivé(e) ce soir. Vous souhaitez calculer la distance que vous avez parcourue dans la journée.

Ce que doit faire votre programme :
Votre programme doit lire deux entiers, correspondant à deux numéros de bornes kilométriques, et il doit afficher la distance séparant ces deux bornes. Notez que le résultat doit être un nombre positif ou nul.

Exemples
Exemple 1
entrée :

152
189
sortie :

37
Exemple 2
entrée :

814
786
sortie :

28


"""

milestone_1 = int(input())
milestone_2 = int(input())
distance = milestone_1 - milestone_2

if distance < 0:
   print(abs(distance))
else:
   print(distance)


"""
L'auberge dans laquelle vous avez prévu de passer la nuit ce soir propose des tarifs très intéressants, pour peu que l'on n'arrive pas trop tard. En effet, plus on arrive tôt moins on devra payer. Vous essayez de construire un programme vous donnant directement le prix à payer en fonction de votre heure d'arrivée.

Ce que doit faire votre programme :
Votre programme lira un entier, l'heure d'arrivée, qui sera compris entre 0 et 12 inclus. 0 correspond à midi, 1 à 1h de l'après-midi, etc. et 12 à minuit.

Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque heure après midi. Il est donc de 15 pièces à 13h, etc. Il ne peut cependant pas dépasser 53 pièces.

Votre programme devra afficher le prix à payer correspondant à l'heure d'arrivée donnée.

Exemples
Exemple 1
entrée :

7
sortie :

45
Exemple 2
entrée :

10
sortie :

53



"""

arrival_time = int(input())
 
bedroom_price = 10 + 5 * arrival_time

if bedroom_price >= 53:
   print(53)
else:
   print(bedroom_price)


""""
À peine arrivé dans le village, voilà qu'une bagarre générale est sur le point d'éclater ! 
Tout en vous mettant à l'abri, vous tâchez de savoir ce qui se passe. On vous explique que le village est principalement composé de deux grandes familles rivales qui ne se supportent pas. 
Tout sujet étant une source de discorde possible, ils avaient décidé que les superficies de leurs champs respectifs ne devaient pas être trop différentes afin de ne pas attiser la jalousie de la famille opposée. 
Mais voilà que le patriarche des Arignon suspecte qu'un des champs des Evaran est trop grand ! Vous décidez de les aider ; mais la tâche ne sera pas facile, chacun gardant jalousement secrète la superficie réelle de ses champs.

Ce que doit faire votre programme :
Votre programme devra lire deux entiers, la superficie d'un champ des Arignon et la superficie d'un champ des Evaran. 
Si l'un des champs est plus grand d'au moins 10 m² (strictement) que l'autre champ, alors il faudra afficher le texte « La famille X a un champ trop grand », « X » devant bien sûr être remplacé par « Arignon » ou « Evaran » selon le cas.

Exemples
Exemple 1
entrée :

42
54
sortie :

La famille Evaran a un champ trop grand
Exemple 2
entrée :

10
20
sortie :

Commentaires
Dans le second exemple, il n'y a rien à afficher.

"""

family_1 = "Arignon"
family_2 = "Evaran"

family_1_area = int(input())
family_2_area = int(input())

area_differential = abs(family_2_area - family_1_area)

if area_differential > 10:

  if family_2_area > family_1_area:
    print(f"La famille {family_2} a un champ trop grand")

  else:
    print(f"La famille {family_1} a un champ trop grand")

# Other way to do it 

first_family = "Arignon"
second_family = "Evaran"

first_family_area = int(input())
second_family_area = int(input())

if second_family_area > first_family_area + 10:
  print(f"La famille {second_family} a un champ trop grand")
if first_family_area > second_family_area + 10:
  print(f"La famille {first_family} a un champ trop grand")


"""
Vous venez d'apprendre qu'un concert de rock va se dérouler ce soir dans la ville située de l'autre côté du lac. Vous avez tout juste le temps d'y arriver en prenant le bateau. Cependant, vous n'êtes pas le seul à vouloir y aller, et il y a une longue queue pour acheter les tickets pour la traversée.

Comme il n'y a qu'une seule personne qui s'occupe à la fois de vendre les tickets et d'aider les gens à monter sur le bateau, vous vous rendez vite compte que vous allez certainement arriver en retard. La vente des tickets est particulièrement lente car il faut demander aux gens leur âge pour savoir s'ils doivent payer plein tarif ou bien tarif réduit.

Vous proposez que votre robot s'occupe de la vente des billets et que la personne responsable du bateau s'occupe uniquement d'aider les gens à monter sur le bateau. Il va donc vous falloir programmer votre robot assez vite pour arriver à temps au concert.

Ce que doit faire votre programme :
Votre programme doit lire l'âge d'une personne et afficher soit « Tarif réduit » si cette personne a strictement moins de 21 ans, soit « Tarif plein » dans le cas contraire.

Exemples
Exemple 1
entrée :

22
sortie :

Tarif plein
Exemple 2
entrée :

16
sortie :

Tarif réduit

"""

age = int(input())

if age < 21:
  print("Tarif réduit")
else:
  print("Tarif plein")


""" Vous arrivez devant un pont que vous devez absolument emprunter pour arriver avant la nuit au village situé de l'autre côté de la rivière. Cependant, la traversée du pont n'est pas gratuite et le tarif dépend de votre chance au jeu. En effet, le gardien vous demande de lancer deux dés et le prix dépendra des valeurs que vous obtiendrez. Vous décidez d'écrire un programme pour vérifier qu'il applique bien le bon tarif.

Ce que doit faire votre programme :
Votre programme doit lire deux entiers, compris entre 1 et 6, la valeur de chaque dé. Si la somme est supérieure ou égale à 10, alors vous devez payer une taxe spéciale (36 pièces). Sinon, vous payez deux fois la somme des valeurs des deux dés. Votre programme devra afficher selon le cas le texte « Taxe spéciale ! » ou bien « Taxe régulière », puis la somme à payer (sans indiquer l'unité).

Exemples
Exemple 1
entrée :

5
6
sortie :

Taxe spéciale !
36
Exemple 2
entrée :

4
3
sortie :

Taxe régulière
14

"""

die_1 = int(input())
die_2 = int(input())
total_dice = die_1 + die_2

if total_dice >= 10:
  print("Taxe spéciale !")
  print(36)
else:
  print("Taxe régulière")
  print(total_dice * 2)

"""
Vous avez passé la nuit dans une auberge. Au petit matin, un championnat de tir à la corde y est organisé. 
Vous ne souhaitez pas participer, mais l'aubergiste insiste pour que vous soyez impliqué dans l'événement. 
Vous décidez alors de vous engager dans les paris qui se font sur les deux équipes qui concourent.

Le championnat oppose deux équipes, contenant chacune autant de joueurs. 
Pour donner de l'allure et pimenter les paris, au début du championnat, tous les joueurs sont présentés, avec leur poids, avant d'aller tenir leur côté de la corde. 
Il est d'abord présenté un membre de la première équipe, puis de la deuxième, puis de la première, puis de la deuxième etc. jusqu'à ce que tous les joueurs soient passés. 
Afin de vous faire un premier pronostic, vous calculez le poids total de chaque équipe, avec votre robot.

Ce que doit faire votre programme :
Votre programme devra lire un premier entier : le nombre de membres nbMembres qui constituent une équipe. 
Ensuite, il devra lire les poids (en kilogrammes), au total nbMembres × 2, sachant que le premier poids est celui d'un joueur de la 1re équipe, le deuxième poids celui d'un joueur de la 2e équipe, le troisième la 1re équipe, le quatrième la 2e équipe, etc.

Après avoir calculé le poids total de chaque équipe, vous devrez afficher le texte « L'équipe X a un avantage » (en remplaçant X par la valeur 1 ou 2), en considérant qu'une équipe est avantagée si elle a un poids total supérieur à celui de l'autre.

Vous afficherez ensuite le texte « Poids total pour l'équipe 1 : » suivi du poids de l'équipe 1, puis « Poids total pour l'équipe 2 : » suivi du poids de l'équipe 2 (voir l'exemple ci-dessous).

On vous garantit que les deux équipes n'auront pas le même poids total.

Exemple
entrée :

3
40
80
50
50
60
10
sortie :

L'équipe 1 a un avantage
Poids total pour l'équipe 1 : 150
Poids total pour l'équipe 2 : 140
Commentaires
Chaque équipe est composée de trois joueurs. 
Ceux de la première pèsent 40, 50 et 60 kg, tandis que ceux de la seconde font 80, 50 et 10 kg. 
Cela fait 150 kg opposés à 140 kg.


"""

members_number = int(input())
total_weights_team_1 = 0
total_weights_team_2 = 0

for _ in range(members_number):
  total_weights_team_1 += int(input())
  total_weights_team_2 += int(input())

if total_weights_team_1 > total_weights_team_2:
  print(f"L'équipe 1 a un avantage")
else:
  print(f"L'équipe 2 a un avantage")

print(f"Poids total pour l'équipe 1 : {total_weights_team_1}")
print(f"Poids total pour l'équipe 2 : {total_weights_team_2}")

"""
Un festin est organisé pour récompenser tous les gens qui ont participé à la construction d'une nouvelle palissade autour du village. Pour empêcher de rentrer ceux qui sont restés toute la journée à la plage au lieu d'aller couper du bois et de planter des piquets, un code secret a été transmis à tous ceux qui ont le droit d'accéder au festin.

Cependant, personne ne veut se dévouer pour garder l'entrée de la salle des fêtes et y filtrer les accès. Personne sauf… votre robot, qui a tendance à surchauffer dès qu'on lui demande de participer à une discussion mondaine ! Programmez donc votre robot pour qu'il ne laisse passer que les gens qui connaissent le code secret.

Ce que doit faire votre programme :
Votre programme doit lire un entier : le code fourni par l'utilisateur. Si ce code correspond au code secret, qui est 64 741, alors le programme devra afficher le texte « Bon festin ! ». Sinon, il devra afficher « Allez-vous en ! ».

Exemples
Exemple 1
entrée :

42
sortie :

Allez-vous en !
Exemple 2
entrée :

64741
sortie :

Bon festin !

"""


secret_code = 64741
entered_code = int(input())

if entered_code != secret_code:
  print("Allez-vous en !")
else:
  print("Bon festin !")