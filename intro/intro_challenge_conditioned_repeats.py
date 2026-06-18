# Utilisation de While

# Il s'agit de faire la même chose plusieurs fois, mais cette fois-ci, on ne sait pas combien de fois il faudra répéter l'action. 
# On va donc utiliser une boucle while.

# On a parfois besoin de répéter certaines instructions jusqu'à ce qu'un certain changement ce soit produit.
# Par exemple, ci-dessous, on va demander à l'utilisateur de saisir un mot de passe. 
# Tant que le mot de passe n'est pas correct, on va lui redemander de le saisir.

# secret = 123456
# password = 0
# while password != secret:
#   print("Tapez le mot de passe :")
#   password = int(input())
# print("Vous avez trouvé !")

# Il est possible d'utiliser des opérateurs booléens pour combiner des conditions et des valeurs booléennes. 
# Voici quelques extraits de code à titre d'exemple :

# while True:
#   print("J'attends")
#   break

# Ce code va répéter l'instruction "J'attends" indéfiniment, car la condition est toujours vraie.
# Il s'agit d'une boucle infinie. Il est possible de l'arrêter en appuyant sur Ctrl+C.
# Il est possible d'utiliser l'instruction break pour sortir de la boucle while.

# secret = 123456
# age = 0
# password = 0

# while password != secret or age <= 3:
#   print("Accès refusé: mauvais mot de passe ou personne trop jeune")
#   age = int(input("Quel âge avez-vous ? "))
#   password = int(input("Tapez le mot de passe :"))


# max_people = 100
# max_temperature = 45

# while people_number <= max_people and temperature <= max_temperature:
#   print("Portes ouvertes")
#   people_number = int(input("Combien de personnes sont présentes ? "))
#   temperature = int(input("Quelle est la température ? "))


""""
Département de médecine : contrôle d'une épidémieDécouverte

Afin de pouvoir mieux combattre les différentes épidémies, parfois très graves, qui se développent régulièrement dans la région, 
le département de médecine de l'université a lancé une grande étude. En particulier, les chercheurs s'intéressent à la vitesse de propagation 
d'une épidémie et donc à la vitesse à laquelle des mesures sanitaires doivent êtres mises en place.

Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier, la population totale de la ville. 
Sachant qu'une personne était malade au jour 1 et que chaque malade contamine deux nouvelles personnes le jour suivant (et chacun des jours qui suivent), 
vous devez calculer à partir de quel jour toute la population de la ville sera malade.

Exemples
Exemple 1
entrée :

3
sortie :

2
Exemple 2
entrée :

10
sortie :

4
Commentaires
On a 1 malade le premier jour, donc 2 nouveaux malades le second jour, soit un total de 3 malades. 
On a donc 6 nouveaux malades au troisième jour, soit un total de 9 malades. On a donc 18 nouveaux malades au quatrième jour, soit…



"""

# population = int(input())
# ill_people = 1
# days_number = 1

# while ill_people < population:
#   ill_people *= 3
#   days_number += 1

# print(days_number)

"""
Administration : comptes annuels

Une grande partie du travail de l'administration de l'université, en plus de gérer les enseignants, les étudiants, les cours… est de veiller au bon fonctionnement de l'université et en particulier à ce que les comptes soient bien tenus. En particulier il faut, une fois par an, faire un bilan annuel des dépenses.

Toutes les dépenses de l'année ont été enregistrées et classées dans une multitude de dossiers et il faut maintenant calculer la somme de toutes ces dépenses. Mais personne ne sait exactement combien de dépenses différentes ont été effectuées durant l'année écoulée !

Ce que doit faire votre programme :
Votre programme devra lire une suite d'entiers positifs et afficher leur somme. On ne sait pas combien il y aura d'entiers, mais la suite se termine toujours par la valeur -1 (qui n'est pas une dépense, juste un marqueur de fin).

Exemples
Exemple 1
entrée :

1000
2000
500
-1
sortie :

3500
Exemple 2
entrée :

-1
sortie :

0


"""

# expense = 0
# total = 0

# while expense != -1:
#   expense = int(input())

#   if expense != -1:
#     total += expense

# print(total)

# Other way to do it

# expense = 0
# total = 0

# while expense != -1:
#   total += expense
#   expense = int(input())

# print(total)


""""
Dans une cité commerçante, il est important que les habitants soient forts en calcul mental afin de pouvoir négocier leurs prix et choisir les meilleurs produits sans se faire avoir. 
Le département de pédagogie de l'université a donc été sollicité afin de mettre au point des exercices stimulants pour les enfants, qui vont les inciter à travailler leur calcul mental.

Réalisant le potentiel que peut avoir votre robot dans un cadre pédagogique, les chercheurs vous demandent de mettre au point un programme capable de faire jouer de manière automatisée un enfant au jeu du « c'est plus, c'est moins » : l'enfant doit deviner un nombre secret en faisant des propositions, et on lui répond chaque fois par « c'est plus » ou « c'est moins », jusqu'à ce qu'il ait trouvé le bon nombre.

L'objectif est bien sûr pour les enfants de trouver le bon nombre le plus rapidement possible !

Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier, le nombre que l'enfant devra trouver. Ensuite, il devra lire les propositions du joueur, et afficher à chaque fois le texte « c'est plus » (l'enfant a proposé un nombre trop petit) ou « c'est moins » (l'enfant a proposé un nombre trop grand) selon les cas, et recommencer tant que l'enfant n'a pas trouvé le bon nombre.

À la fin, il faudra afficher le texte « Nombre d'essais nécessaires : » puis, à la ligne en dessous, le nombre d'essais qui ont été nécessaires.

On vous garantit que l'enfant finira par trouver la bonne valeur !

Exemples
Exemple 1
entrée :

5
1
2
3
4
5
sortie :

c'est plus
c'est plus
c'est plus
c'est plus
Nombre d'essais nécessaires :
5
Exemple 2
entrée :

10
5
15
8
12
11
10
sortie :

c'est plus
c'est moins
c'est plus
c'est moins
c'est moins
Nombre d'essais nécessaires :
6
Exemple 3
entrée :

-50
-80
-50
sortie :

c'est plus
Nombre d'essais nécessaires :
2



"""

# secret_number = int(input())
# total_trials = 0

# trial = -1

# while trial != secret_number:
#   trial = int(input())
#   total_trials += 1

#   if trial < secret_number:
#     print("c'est plus")
#   elif trial > secret_number:
#     print("c'est moins")
   
  
# print("Nombre d'essais nécessaires :")
# print(total_trials)

"""
Les habitants adorent les constructions en forme de pyramide ; de nombreux bâtiments officiels ont d'ailleurs cette forme. 
Pour fêter les 150 ans de la construction de la ville, le gouverneur a demandé la construction d'une grande et majestueuse pyramide à l'entrée de la ville. 
Malheureusement, en ces périodes de rigueur budgétaire, il y a peu d'argent pour ce projet. 
Les architectes souhaitent cependant construire la plus grande pyramide possible étant donné le budget prévu.


"""

# max_stones_number = int(input())
# number_of_stage = 0
# necessary_stones = 0

# while necessary_stones + (number_of_stage + 1) ** 2 <= max_stones_number:
#   number_of_stage += 1
#   necessary_stones += number_of_stage ** 2

# print(number_of_stage)
# print(necessary_stones) 

"""

Département de chimie : mélange explosif

Les chimistes de l'université ont mis au point un nouveau procédé de fabrication d'un onguent qui permet une cicatrisation très rapide des blessures. Ce procédé est cependant très long et nécessite une surveillance de tous les instants de la préparation en train de chauffer, et ce parfois pendant des heures. 
Confier cette tâche à un étudiant n'est pas possible, ils s'endorment toujours ou ne font pas attention… et cela risque alors d'exploser !

Un dispositif automatique de surveillance de la préparation serait donc intéressant. 
Celui-ci surveillerait la température toutes les 15 secondes, et si celle-ci devient anormale alors une alarme devrait sonner, afin de prévenir tout le monde.

Ce que doit faire votre programme :
Votre programme devra lire trois entiers : le nombre total de mesures envisagées ainsi que la température minimum et maximum autorisées. 
Les entiers suivants seront les différentes températures relevées au cours du temps.

Tant que les températures relevées restent dans le bon intervalle, votre programme devra écrire le texte « Rien à signaler », mais dès que la température n'est pas bonne il doit écrire le texte « Alerte !! » et s'arrêter.

Exemples
Exemple 1
entrée :

5
10
20
15
10
20
0
15
sortie :

Rien à signaler
Rien à signaler
Rien à signaler
Alerte !!
Exemple 2
entrée :

3
0
100
15
50
75
sortie :

Rien à signaler
Rien à signaler
Rien à signaler

"""

# temperature_collection = int(input())
# min_temp = int(input())
# max_temp = int(input())

# for temperature in range(temperature_collection):
#   temperature = int(input())
#   if min_temp <= temperature <= max_temp:
#     print("Rien à signaler")
#   else:
#     print("Alerte !!")
#     break

# Other way to do it:

temperature_collection = int(input())
min_temp = int(input())
max_temp = int(input())

picking_number = 0

while picking_number < temperature_collection:
  temperature = int(input())

  if min_temp <= temperature <= max_temp:
    print("Rien à signaler")
  else:
    print("Alerte !!")
    break

  picking_number += 1

# Other way to do it:

# temperature_collection = int(input())
# min_temp = int(input())
# max_temp = int(input())

# picking_number = 0

# temperature_is_ok = True

# while picking_number < temperature_collection and temperature_is_ok:
#   temperature = int(input())

#   if min_temp <= temperature <= max_temp:
#     print("Rien à signaler")
#   else:
#     print("Alerte !!")
#     temperature_is_ok = False

#   picking_number += 1
