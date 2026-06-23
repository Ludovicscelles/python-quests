# using for loop

# Afficher les nombres de 0 à 9

print("Affichage des nombres de 0 à 9")
for nombre in range(0, 10, 1):
    print(nombre) # On va donc de 0 (inclus) à 10 (exclus) et en faisant un pas de 1

# Afficher les nombres de 10 à 20

print("Affichage des nombres de 10 à 20")
for nombre in range(10, 21, 1):
    print(nombre) # On va donc de 10 (inclus) à 21 (exclus) et en faisant un pas de 1


# Afficher les nombres pairs de 100 à 120

print("Affichage des nombres pairs de 100 à 120")
for nombre in range(100, 121, 2):
    print(nombre) # On va donc de 100 (inclus) à 121 (exclus) et en faisant un pas de 2


# Afficher les multiples de 5 de 20 à -20

print("Affichage des multiples de 5 de 20 à -20")
for nombre in range(20, -21, -5):
    print(nombre) # On va donc de 20 (inclus) à -21 (exclus) et en faisant un pas de -5

print("Affichage des nombres de 0 à 9")
for nombre in range(10):  
    print(nombre) # On va donc de 0 (inclus) à 10 (exclus) et en faisant un pas de 1

# Si on a un début à 0 et un pas de 1, on peut omettre ces deux paramètres et juste mettre le nombre de fin

print("Affichage des nombres de 0 à 9")
for nombre in range(10):
    print(nombre) # On va donc de 0 (inclus) à 10 (exclus) et en faisant un pas de 1


"""
Préparation de l'onguent

Parmi les chimistes de l'université, le plus expérimenté est Alcophante et c'est donc lui qui a la charge de la préparation de l'onguent guérisseur. 
Malheureusement, il connait quelques problèmes de mémoire et ne se souvient jamais quelle quantité de chaque ingrédient il faut mettre ! 
Afin de l'aider, vous décidez de programmer votre robot pour qu'il puisse répondre à Alcophante, à chaque fois que celui-ci en aura besoin.

Ce que doit faire votre programme :
Il y a 10 ingrédients dans la recette et les quantités nécessaires pour chacun sont (en grammes) : 500, 180, 650, 25, 666, 42, 421, 1, 370 et 211.

Votre programme doit lire un entier, le numéro d'un ingrédient (compris entre 0 et 9) et afficher la quantité associée à cet ingrédient.

Exemple
entrée :

3
sortie :

25

"""

ingredients = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]

ingredients_nb = int(input())

if 0 <= ingredients_nb < len(ingredients):
    print(ingredients[ingredients_nb])
else:
    print("Indice invalide")


"""
Liste de courses

Les stocks des ingrédients nécessaires à la réalisation de l'onguent commencent à se vider et les savants vous chargent d'aller en ville acheter une certaine quantité de chaque ingrédient, afin de pouvoir continuer la production pendant le prochain mois.

Le comptable étant particulièrement pointilleux, il vous donnera exactement la quantité d'argent dont vous avez besoin, pas une pièce de plus. Heureusement vous savez à l'avance le prix de chaque ingrédient et la quantité dont vous avez besoin.

Ce que doit faire votre programme :
Il y a 10 ingrédients et ils ont tous un prix au kilo différent : 9, 5, 12, 15, 7, 42, 13, 10, 1 et 20.

Votre programme devra lire 10 entiers, le poids (en kilogrammes) qu'il faut acheter pour chaque ingrédient. Il devra calculer le coût total de ces achats.

Exemple
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
sortie :

134

"""

ingredients_price_kg = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]

total_price = 0

for price in ingredients_price_kg:

    ingredient_weight = int(input())

    total_price += price * ingredient_weight

print(total_price)

""""
Grand inventaire

Vous êtes dans la boutique du plus grand marchand de la ville, à la recherche d'un certain nombre d'ingrédients. Malheureusement pour vous, c'est la période du grand inventaire et cela peut durer très longtemps ! Vous décidez de les aider. À partir du livre de comptes, sur lequel sont indiqués toutes les ventes et achats de chaque produit, vous allez pouvoir rapidement vérifier si les quantités restantes dans les étalages sont bien les bonnes et s'il n'y a pas eu de vols.

Ce que doit faire votre programme :
Un livre de comptes décrit les achats et ventes successives de 10 produits numérotés de 1 à 10. Le livre décrit les opérations depuis une situation où le stock de chacun des produits était de zéro.

Chaque ligne du livre de comptes décrit l'achat (augmentation du stock) ou la vente (réduction du stock) d'une certaine quantité de l'un des produits.

Votre objectif est de déterminer pour chaque produit, la quantité restant dans le stock à l'issue de l'ensemble de ces achats et ventes.

Entrée
La première ligne contient un entier nbOperations : le nombre d'opérations décrites dans le livre de comptes.

Suivent ensuite nbOperations paires d'entiers, où le premier entier de chaque paire est le numéro de l'ingrédient concerné par l'opération, et le deuxième est la quantité. Si la quantité est négative, l'opération est une vente, et si elle est positive, l'opération est un achat du produit indiqué.

Sortie
Vous devez afficher 10 entiers sur la sortie : la quantité restante pour chacun des produits dans l'ordre de leur numéro, une fois l'ensemble des opérations décrites dans le livre effectuées.

Exemple
entrée :

5
1
100
2
50
1
-50
3
20
2
-10
sortie :

50
40
20
0
0
0
0
0
0
0

"""

account_book = [0] * 11

number_of_operations = int(input())

for operation in range (number_of_operations):
    product_number = int(input())
    product_quantity = int(input())

    account_book[product_number] += product_quantity

for product_number in range(1, 11):
    print(account_book[product_number])

"""
Étude de marché

Afin de partir dans un long voyage, à la recherche de produits exotiques, les marchands prévoient toujours d'emmener avec eux des produits locaux afin de les vendre au cours du trajet. 
Pour décider quels produits emmener, ils ont fait une petite étude de marché auprès de la population, en demandant à chaque personne d'indiquer LE produit qu'elle serait prête à acheter (celui qu'elle préfère donc).

Ce que doit faire votre programme :
On vous donne le numéro du produit préféré par différentes personnes. 
Écrivez un programme qui indique pour chaque numéro de produit, le nombre de personnes dont c'est le produit préféré.

Entrée
Les deux premiers entiers à lire sont le nombre total de produits nbProduits et le nombre de personnes nbPersonnes (nbPersonnes <= 1000) ayant exprimé leur souhait.

On lit ensuite nbPersonnes entiers : les numéros des produits préférés des différentes personnes. 
Les produits sont numérotés de 0 à nbProduits - 1.

Sortie
Vous devez afficher nbProduits entiers : pour chaque produit dans l'ordre de leur numéro, affichez le nombre de personnes qui le préfèrent.

Exemple
entrée :

4
10
0
2
2
1
2
2
0
2
3
0
sortie :

3
1
5
1

"""

total_products = int(input())
product_scores = [0] * total_products

total_people = int(input())

for people in range(total_people):
    preferred_product = int(input())

    product_scores[preferred_product] += 1

for score in product_scores:
    print(score)

"""

Répartition du poids

Après seulement quelques heures de route, au sein de cette longue caravane de marchands, certains chevaux montrent déjà des signes de fatigue alors que d'autres sont en pleine forme. 
En cherchant la raison de ce phénomène, vous vous rendez compte que certaines charrettes sont bien plus lourdes que les autres ! Vous décidez donc de mieux répartir le poids, afin que toutes les charrettes aient exactement le même poids.

Ce que doit faire votre programme :
On vous décrit les charrettes qui composent une caravane, en vous donnant pour chacune, le poids des marchandises qu'elle transporte.

Votre programme doit déterminer quel poids ajouter ou retirer à chaque charrette, pour qu'elles transportent toutes ensuite le même poids, et ce sans modifier le poids total transporté par l'ensemble des charrettes de la caravane.

Entrée
L'entrée commence par un entier nbCharrettes (nbCharrettes <= 3000) : le nombre de charrettes de la caravane.

Les nbCharrettes lignes suivantes décrivent chacune une charrette par un nombre décimal : le poids qu'elle transporte initialement.

Sortie
Vous devez afficher nbCharrettes nombres décimaux sur la sortie : le poids à ajouter à chaque charrette (ce qui revient à en retirer si ce nombre est négatif), dans le même ordre que celui de l'entrée. Il n'y a pas d'arrondis à faire.

Exemple
entrée :

5
40.0
12.0
20.0
5.0
33.0
sortie :

-18.0
10.0
2.0
17.0
-11.0
Commentaires
Dans cet exemple, on modifie toutes les charettes pour qu'elles transporte chacune un poids de 22.0, soit un total de 110 pour la caravane, comme au départ.


"""

carts_number = int(input())
total_weight = 0
cart_weights = []

for cart in range(carts_number):
    cart_weight = float(input())
    cart_weights.append(cart_weight)
    total_weight += cart_weight

average_weight = total_weight / carts_number

adjustments = []

for cart_weight in cart_weights:
    adjustment = average_weight - cart_weight
    adjustments.append(adjustment)

for adjustment in adjustments:
    print(adjustment)

"""
Visite de la mine

L'un des produits nécessaires pour la fabrication de l'onguent magique, un minerai très rare, ne se trouve qu'en un seul endroit sur la planète, au fond de la plus vieille mine existante, jadis exploitée par le peuple nain. 
Désormais seuls quelques uns d'entre eux sont encore sur place, afin de guider les voyageurs (commerçants et touristes) au sein de ce dédale de cavernes et galeries.

Après avoir engagé un guide, il vous mène jusqu'à l'endroit prévu mais un petit désaccord sur le paiement de ses services le pousse à vous laisser sur place, sans aucune chance de retrouver la sortie. Heureusement votre robot à conservé en mémoire la suite des déplacements qui vous ont amené de l'entrée jusqu'à votre position actuelle, il ne vous reste plus qu'à suivre le chemin inverse !

Ce que doit faire votre programme :
Il existe 5 types de déplacements, représentés par 5 entiers différents : aller à gauche (1), aller à droite (2), aller tout droit (3), monter (4) et descendre (5).

Le premier entier à lire est le nombre total de déplacements (1000 au maximum). 
Ensuite, chaque déplacement (représenté par un entier) est indiqué sur sa propre ligne.

Vous devez afficher la suite des déplacements à faire pour aller de votre position actuelle à la sortie.

Exemple
entrée :

6
1
3
2
4
4
5
sortie :

4
5
5
1
3
2

"""

# moves_number = int(input())

# opposites = {
#     1: 2,
#     2: 1,
#     3: 3,
#     4: 5,
#     5: 4
# }

moves_to_go_out = []

for move in range (moves_number):
    move_in = int(input())
    moves_to_go_out.append(opposites[move_in])

for move in reversed(moves_to_go_out):
    print(move)

# Other way to do it:

reversed_moves = [0, 2, 1, 3, 5, 4]

moves_number = int(input())

way_out = [0] * moves_number

for move in range(moves_number):
    way_out[move] = int(input())

for move in range(moves_number-1, -1, -1):
    move_out = way_out[move]
    print(reversed_moves[move_out])

"""
Journée des cadeaux

Dans la ville de Largition, la tradition veut que, une fois par mois, les habitants les plus riches fassent un cadeau aux habitants les moins riches. 
Cela permet de maintenir une bonne ambiance malgré les inévitables différences de richesses.

Un habitant est considéré comme riche si sa fortune est plus grande que celle de la moitié de la population. 
Calculer, chaque mois, qui est riche ou pas est un long travail, aussi lorsque le maire a entendu parlé de vos talents, il vous a demandé votre aide.

Ce que doit faire votre programme :
Il devra lire un premier entier, le nombre d'habitants (au plus 1000) puis, pour chaque habitant il devra lire sa fortune, un entier. 
Il devra calculer puis afficher une valeur permettant de dire facilement si une personne est riche ou pas, simplement en regardant si la fortune de cette personne est plus grande ou plus petite que cette valeur.

Deux cas peuvent se présenter :

Si le nombre d'habitants est impair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3 alors la valeur recherchée est 8. 
En effet, il y aura alors 2 personnes "riches" (10 et 12), 2 "moins riches" (3 et 5) et 1 juste au milieu (8) qui ne donnera ni recevra de cadeau.
Si le nombre d'habitants est pair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3, 9 alors la valeur recherchée est entre 8 et 9. 
Il y a en effet 3 personnes "riches" (9, 10 et 12) et 3 "moins riches" (3, 5 et 8). Par convention on prendra la valeur 8.5, c'est-à-dire la moyenne de 8 et 9.

Exemples
Exemple 1
entrée :

5
10
5
12
8
3
sortie :

8
Exemple 2
entrée :

6
10
5
12
8
3
9
sortie :

8.5


"""

population = int(input())
fortune_list = [0] * population

for people in range(population):
    fortune = int(input())
    fortune_list[people] = fortune

fortune_list.sort()

if population % 2 != 0:
    median_wealth = fortune_list[population // 2]
else:
    median_wealth = (fortune_list[population // 2] + fortune_list[(population // 2) - 1])/2

print(median_wealth)


"""
Course à trois jambes

En parallèle du grand marché de la ville auquel vous accompagnez vos amis marchands, un ensemble de jeux sont organisés pour les habitants, 
en particulier la fameuse « course à trois jambes » : cette course se déroule par équipes de deux personnes dont deux des jambes sont attachées par une corde :


Afin de constituer les équipes au hasard, un tirage au sort est organisé. 
Comme c'est une opération longue à faire manuellement et que vous êtes impatient, vous décidez d'aider les organisateurs avec votre robot.

Ce que doit faire votre programme :
Le premier entier à lire est le nombre de participants (au plus 3 000) qui sera toujours pair. 
Ensuite il faut lire, pour chaque participant, un entier qu'il a choisi librement.

Les équipes sont constituées ainsi : la personne ayant choisi le plus petit entier est avec celle ayant choisi le plus grand, 
celle ayant choisi le deuxième plus petit est avec celle ayant choisi le deuxième plus grand, et ainsi de suite.

Vous devrez afficher la composition de chacune des équipes, dans l'ordre : d'abord celle dont le plus petit numéro fait partie, 
puis celle dont le second plus petit numéro fait partie, et ainsi de suite. Au sein de chaque équipe on affichera d'abord le plus petit numéro puis le plus grand.

On vous garantit que tous les numéros sont différents.

Exemple
entrée :

10
80
1000
5
154
130
847
450
42
35
789
sortie :

5 1000
35 847
42 789
80 450
130 154

"""

participants = int(input())
numbers = [0] * participants

for participant in range(participants):
    number = int(input())
    numbers[participant] = number

increasing_numbers = sorted(numbers)[:len(numbers)//2]

decreasing_numbers = sorted(numbers, reverse=True)[:len(numbers)//2]

for number_i, number_d in zip(increasing_numbers, decreasing_numbers):
    print("{} {}".format(number_i, number_d))

# Other way to do it:

participants = int(input())
numbers = [0] * participants

for participant in range(participants):
    number = int(input())
    numbers[participant] = number

numbers.sort()

for first_participant in range(participants//2):
    second_participant = participants - 1 - first_participant
    print("{} {}".format(numbers[first_participant], numbers[second_participant]) )


"""
Banquet municipal

Vous commencez à être connu pour vos talents de programmeur, aussi lors de votre passage dans la ville d'Incerto, le maire décide de vous inviter au grand banquet qu'il organise. Le maire se charge lui-même de faire le plan de table mais il change toujours d'avis et les serveurs doivent constamment changer de place les petites affiches sur lesquelles sont indiqués les noms des personnes.

Afin de l'aider, vous lui proposez d'utiliser votre robot pour déterminer la position de chaque personne après tous les changements décidés par le maire.

Afin de simplifier le problème, on suppose que chaque personne est identifiée par un numéro et qu'il n'y a qu'une seule très grande table.

Ce que doit faire votre programme :
Votre programme devra lire deux entiers : le nombre total de positions sur la table (au maximum 1000) et le nombre de changements de positions. Il devra ensuite lire, pour chaque position, un entier : le numéro de la personne qui doit, actuellement, s'installer à cette position.

Il faut lire ensuite les changements exprimés sous la forme de deux entiers chacun : position1 et position2. Un changement (position1, position2) signifie que les deux personnes qui étaient à ses positions doivent échanger leurs places (les positions sont indexées à partir de 0).

Vous devrez afficher, pour chaque position, le numéro de la personne qui s'y trouve une fois tous les changements faits.

Exemple
entrée :

5
3
1
2
3
4
5
1
2
1
3
4
0
sortie :

5
4
2
3
1
Commentaires
Evolution des numéros dans l'exemple :

Au début : 1,2,3,4,5
Après le changement (1, 2) : 1,3,2,4,5
Après le changement (1, 3) : 1,4,2,3,5
Après le changement (4, 0) : 5,4,2,3,1



"""

total_positions = int(input())
total_moves = int(input())

positions = [0] * total_positions

for position in range(total_positions):
    position_number = int(input())
    positions[position] = position_number

for move in range(total_moves):
    first_guest = int(input())
    second_guest = int(input())
    positions[first_guest], positions[second_guest] = positions[second_guest], positions[first_guest]


for person in positions:
    print(person)

"""
Choix des emplacements

Lorsqu'on organise un marché, certains emplacements sont beaucoup plus intéressants que d'autres. 
Afin d'éviter les tentations de « pots de vin », la ville dans laquelle vous venez d'arriver a décidé qu'on organiserait à chaque fois un tirage au sort, chacun ayant sa chance !

Chaque marchand met donc son nom dans un grand panier, et des tirages sont effectués. 
On tire d'abord le nom du marchand qui aura le premier emplacement, puis celui qui aura le second, et ainsi de suite. 
On décide alors d'afficher par ordre alphabétique, les noms des marchands avec le numéro de leur emplacement.

Pour simplifier l'exercice, on suppose que les marchands ne mettent pas leur nom dans le panier mais simplement un numéro qui indique leur rang dans la liste des marchands.

Ce que doit faire votre programme :
Votre programme devra lire le nombre d'emplacements nbEmplacements (au maximum 1 000), puis pour chaque emplacement à partir de 0, le numéro du marchand à qui est attribué l'emplacement (entre 0 et nbEmplacements − 1).

Ensuite, pour chaque marchand de 0 à nbEmplacements − 1, votre programme devra afficher le numéro de l'emplacement qui lui est attribué.

Exemple
entrée :

5
1
4
0
3
2
sortie :

2
0
4
3
1
Commentaires
Il y a 5 positions : la première est utilisée par le marchand 1, la seconde est utilisée par le marchand 4, la troisième le marchand 0, etc.

En sortie, on donne les positions des marchands par ordre des numéros des marchands :

marchand n°0 : position 2 ;
marchand n°1 : position 0 ;
marchand n°2 : position 4 ;
marchand n°3 : position 3 ;
marchand n°4 : position 1.

"""
# initialize the number of total spots and create a list to hold the sellers' positions
total_spots = int(input())
sellers_position = [0] * total_spots

# read the seller numbers for each spot and store their positions in the list
for i_spot in range(total_spots):
    seller_number = int(input())
    sellers_position[seller_number] = i_spot

# print the positions of the sellers in order of their numbers
for i_spot in sellers_position:
    print(i_spot)