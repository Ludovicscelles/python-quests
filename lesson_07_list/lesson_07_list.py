# les listes

# créer une liste
ma_liste = [1, 2, 3, 4, 5]
print(ma_liste)


# enumerate

fruits = ["pomme", "banane", "orange", "kiwi", "fraise", "coco", "mangue", "ananas", "papaye", "melon"]
for i, valeur in enumerate(fruits):
  print(i, valeur)

  # La fonction enumerate() est utilisée pour ajouter un compteur aux objets itérables comme une liste.
  # Cette fonction simplifie la gestion des index et des éléments lors de l'utilisation de boucles, en renvoyant un objet énuméré 
  # qui comprend les index et les valeurs des objets itérables



  vegetables = ["carotte", "brocoli", "épinard", "tomate", "concombre", "poivron", "courgette", "aubergine", "chou-fleur", "navet"]
  print()

  for i, valeur in enumerate(vegetables, 11):
    print(i, valeur)

  # Il est également possible de spécifier un point de départ pour le compteur


  # range

  # La fonction range est souvent utilisée avec les boucles for. Elle permet de générer des séquences de n éléments.
  # Elle s'utilise avec un, deux ou trois arguments : range(start, end, step).
  # - start : le point de départ de la séquence (inclusif). Par défaut, il est égal à 0.
  # - end : le point d'arrêt de la séquence (exclusif). C'est l'argument obligatoire.
  # - step : le pas entre les éléments de la séquence. Par défaut, il est égal à 1.
  # Sur une liste, on peut utiliser la fonction range pour itérer sur les indices des éléments de la liste. 
  # Par exemple, pour afficher les indices de la liste soda, on peut faire :

soda = ["coca-cola", "pepsi", "sprite", "fanta", "7up", "dr pepper", "mountain dew", "root beer", "ginger ale", "sierra mist"]

# range (stop)

for i in range(len(soda)):
  print(i)


# Avec un seul argument, range génère une séquence de nombres de 0 à stop-1. 
# Dans ce cas, len(soda) renvoie la longueur de la liste soda, qui est 10. 
# Donc, range(len(soda)) génère une séquence de nombres de 0 à 9, ce qui correspond aux indices des éléments de la liste soda.


# append

# append() est une fonction de la bibliothèque NumPy qui permet d'ajouter des éléments à la fin d'un tableau existant

wine = ["merlot", "cabernet sauvignon", "pinot noir", "chardonnay", "sauvignon blanc", "riesling", "syrah", "zinfandel", "malbec", "tempranillo"]
print()
print(wine)
print()

wine.append("grenache")
print(wine)
print()

wine.append("cinsault")
print(wine)
print()


# del

# La fonction del est utilisée pour supprimer des éléments d'une liste en fonction de leur index.
# Par exemple, pour supprimer le troisième élément de la liste wine, on peut faire :

del wine[2]
print(wine)
print()

del wine[5]
print(wine)
print()

# random.randint

# La fonction random.randint(a, b) génère un nombre entier aléatoire compris entre a et b (inclus).
# Par exemple, pour générer un nombre entier aléatoire entre 1 et 10, on peut faire :

import random
random_number = random.randint(1, 10)
print(random_number)
print()

random_number_02 = random.randint(252, 300)
print(random_number_02)
print()

random_index_wine = random.randint(0, len(wine) - 1)
print(random_index_wine)
print(wine[random_index_wine])
print()


# insert

# La fonction insert() est utilisée pour insérer des valeurs dans un tableau à des positions spécifiées le long d'un axe donné.

juice = ["orange", "pomme", "raisin", "ananas", "mangue", "fraise", "kiwi", "coco", "papaye", "melon"]
print(juice)

juice.insert(2, "citron")
print(juice)
print()

juice.insert(5, "pamplemousse")
print(juice)
print()


# join

# La méthode join() est une méthode de chaîne de caractères utilisée pour concaténer les éléments d'une séquence, 
# comme une liste ou un tuple, en une seule chaîne de caractères.

desserts = ["gâteau", "tarte", "crème brûlée", "mousse au chocolat", "éclair", "macaron", "profiterole", "tiramisu", "pavlova", "cheesecake"]
print(desserts)
separator = ", "
desserts_string = separator.join(desserts)
print(desserts_string)
print()

# La méthode join() prend une séquence d'éléments (dans ce cas, la liste desserts) et les concatène en une seule chaîne de caractères,
# en utilisant la chaîne de caractères spécifiée (dans ce cas, ", ") comme séparateur entre les éléments de la séquence. 
# Le résultat est une chaîne de caractères qui contient tous les éléments de la liste desserts séparés par une virgule et un espace.


# split

# La méthode split() est une méthode qui permet de diviser une chaîne de caractères en une liste de sous-chaînes en se basant sur un séparateur.
# Par défaut, ce séparateur est l'espace blanc.

starches = "maïs, pomme de terre, riz, blé, avoine, orge, quinoa, millet, sarrasin, amarante, patate douce"
print(starches)
separator = ", "
starches_list = starches.split(separator)
print(starches_list)
print()

# mutable

# Les listes sont des objets mutables, ce qui signifie que vous pouvez modifier leur contenu après les avoir créées.
# Par exemple, vous pouvez ajouter, supprimer ou modifier des éléments d'une liste existante.
# L'id de la liste reste le même, même si son contenu change.

condiments = ["sel", "poivre", "paprika", "cumin", "curcuma", "cannelle", "gingembre", "ail en poudre", "oignon en poudre", "piment de cayenne"]
print(condiments)
print(id(condiments))
print()

condiments[0] = "sel de mer"
print(condiments)
print(id(condiments))
print()

condiments.append("herbes de Provence")
print(condiments)
print(id(condiments))

# list of lists

# Une liste de listes est une liste qui contient d'autres listes comme éléments.
# Par exemple, une liste de sauces peut être une liste qui contient trois listes de sauces différentes : sauces_01, sauces_02 et sauces_03.

sauces_01 = ["bolognese", "carbonara", "alfredo", "pesto", "marinara", "arrabbiata", "puttanesca", "amatriciana", "napolitaine", "primavera"]
sauces_02 = ["béchamel", "hollandaise", "velouté", "espagnole", "soubise", "mornay", "sauce gribiche", "sauce ravigote", "sauce grise", "sauce blanche"]
sauces_03 = ["sauce barbecue", "sauce teriyaki", "sauce soja", "sauce hoisin", "sauce sriracha", "sauce chili", "sauce aigre-douce", "sauce satay", "sauce yakitori", "sauce ponzu"]

sauces = [sauces_01, sauces_02, sauces_03]
print(sauces)
print()
print(sauces[0])
print()
print(sauces[1])
print()
print(sauces[2])
print()
print(sauces[0][0])
print()
print(sauces[1][0])
print()
print(sauces[2][0])
print()

# iterate a list

# Pour itérer sur une liste, on peut utiliser une boucle for.
# Par exemple, pour afficher les éléments de la liste hot_drinks, on peut faire :

hot_drinks = ["café", "thé", "chocolat chaud", "lait chaud", "tisane", "matcha latte", "chai latte", "cappuccino", "latte macchiato", "americano"]
for drink in hot_drinks:
  print(drink)

print()

# Pour itérer, on peut également utiliser une boucle while avec un index pour accéder aux éléments de la liste.
index = 0
while index < len(hot_drinks):
  print(hot_drinks[index])
  index += 1

# reverse a list

# Pour inverser une liste, on peut utiliser la fonction reversed() ou la méthode reverse().
# La fonction reversed() renvoie un itérateur qui parcourt la liste à l'envers, tandis que la méthode reverse() modifie la liste en place.

hot_drinks_reversed = list(reversed(hot_drinks))
print(hot_drinks_reversed)
print()

hot_drinks.reverse()
print(hot_drinks) 