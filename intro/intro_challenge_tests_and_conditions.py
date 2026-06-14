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

# packages_number = int(input())
# weight_of_a_package = int(input())
# total_weight = packages_number * weight_of_a_package
# alert = str("Surcharge !")

# if total_weight > 105:
#    print(alert)


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

# milestone_1 = int(input())
# milestone_2 = int(input())
# distance = milestone_1 - milestone_2

# if distance < 0:
#    print(abs(distance))
# else:
#    print(distance)


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

# arrival_time = int(input())
 
# bedroom_price = 10 + 5 * arrival_time

# if bedroom_price >= 53:
#    print(53)
# else:
#    print(bedroom_price)


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

# family_1 = "Arignon"
# family_2 = "Evaran"

# family_1_area = int(input())
# family_2_area = int(input())

# area_differential = abs(family_2_area - family_1_area)

# if area_differential > 10:

#   if family_2_area > family_1_area:
#     print(f"La famille {family_2} a un champ trop grand")

#   else:
#     print(f"La famille {family_1} a un champ trop grand")

# Other way to do it 

first_family = "Arignon"
second_family = "Evaran"

first_family_area = int(input())
second_family_area = int(input())

if second_family_area > first_family_area + 10:
  print(f"La famille {second_family} a un champ trop grand")
if first_family_area > second_family_area + 10:
  print(f"La famille {first_family} a un champ trop grand")


