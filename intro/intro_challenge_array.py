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

# ingredients = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]

# ingredients_nb = int(input())

# if 0 <= ingredients_nb < len(ingredients):
#     print(ingredients[ingredients_nb])
# else:
#     print("Indice invalide")


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

# ingredients_price_kg = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]

# total_price = 0

# for price in ingredients_price_kg:

#     ingredient_weight = int(input())

#     total_price += price * ingredient_weight

# print(total_price)

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



