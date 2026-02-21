# dictionnaries

# dictionnaries sont des structures de données qui stockent des paires clé-valeur. 
# Ils sont utilisés pour représenter des données structurées et permettent un accès rapide aux valeurs associées à des clés spécifiques.

# .keys()

# La méthode .keys() est utilisée pour obtenir une vue des clés d'un dictionnaire.
# Par exemple, si nous avons un dictionnaire appelé "personne" avec des clés "nom", "âge" et "ville", nous pouvons utiliser .keys() pour obtenir une liste des clés :

personne = {"nom": "Alice", "âge": 30, "ville": "Paris"}
print(personne.keys())
print()

# Si nous avons un dictionnaire appelé "cake" avec des clés "gâteau", "pâte" et "garniture", nous pouvons utiliser .keys() pour obtenir une liste des clés :

cake = {"gâteau": "chocolat", "pâte": "sablée", "garniture": "fruits rouges"}
print(cake.keys())
print()

# .values()

# La méthode .values() est utilisée pour obtenir une vue des valeurs d'un dictionnaire.
# Par exemple, si nous avons un dictionnaire appelé "personne" avec des clés "nom", "âge" et "ville", 
# nous pouvons utiliser .values() pour obtenir une liste des  valeurs :

print(personne.values())
print()  

# Si nous avons un dictionnaire appelé "cake" avec des clés "gâteau", "pâte" et "garniture", nous pouvons utiliser .values() pour obtenir une liste des valeurs :
print(cake.values())
print()


# .items()

# La méthode .items() est utilisée pour obtenir une vue des paires clé-valeur d'un dictionnaire.
# Par exemple, si nous avons un dictionnaire appelé "personne" avec des clés "nom", "âge" et "ville", nous pouvons utiliser .items() pour obtenir une liste des paires clé-valeur :

print(personne.items())
print()

# Si nous avons un dictionnaire appelé "cake" avec des clés "gâteau", "pâte" et "garniture", nous pouvons utiliser .items() pour obtenir une liste des paires clé-valeur :
print(cake.items())
print()


# boucle imbriquée

# Une boucle imbriquée est une boucle à l'intérieur d'une autre boucle.
# Par exemple, si nous avons une liste de dictionnaires représentant des personnes, nous pouvons utiliser une boucle imbriquée pour parcourir chaque personne et afficher ses informations :
personnes = [
    {"nom": "Alice", "âge": 30, "ville": "Paris"},
    {"nom": "Bob", "âge": 25, "ville": "Londres"},
    {"nom": "Charlie", "âge": 35, "ville": "New York"}
]

for personne in personnes:
    print("Nom:", personne["nom"])
    print("Âge:", personne["âge"])
    print("Ville:", personne["ville"])
    print()

# Si nous avons une liste de dictionnaires représentant des gâteaux, nous pouvons utiliser une boucle imbriquée pour parcourir chaque gâteau et afficher ses informations :
cakes = [
    {"gâteau": "chocolat", "pâte": "sablée", "garniture": "fruits rouges"},
    {"gâteau": "vanille", "pâte": "brisée", "garniture": "crème pâtissière"},
    {"gâteau": "citron", "pâte": "feuilletée", "garniture": "meringue"}
]
for cake in cakes:
    print("Gâteau:", cake["gâteau"])
    print("Pâte:", cake["pâte"])
    print("Garniture:", cake["garniture"])
    print()