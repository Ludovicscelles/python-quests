# dictionnaries

# dictionnaries sont des structures de données qui stockent des paires clé-valeur. 
# Ils sont utilisés pour représenter des données structurées et permettent un accès rapide aux valeurs associées à des clés spécifiques.

# Un dictionnaire est défini en utilisant des accolades {} et les paires clé-valeur sont séparées par des virgules.
# Dans l'exemple ci-dessous, nous avons 5 clés, chacune ayant une seule valeur attribuée.

# Par exemple, la clé "Alex" referme la valeur 5.

my_dict = {
    "Alex": 5,
    "Ben": 10,
    "Carly": 12,
    "Danielle": 7,
    "Evan": 6
}

print()
print(my_dict)

# Regardons de plus près les différences entre un dictionnaire et une liste.

grades_dictionary = {
    "John": "A",
    "Emily": "A+",
    "Betty": "B",
    "Mike": "C",
    "Ashley": "A"

}

grades_list = ["A", "A+", "B", "C", "A"]

print()
print("Résultat pour Betty via le dictionnaire : ",grades_dictionary["Betty"])
print()

print("Résultat pour Betty via la liste : ",grades_list[2])
print()

# L'utilisation d'un dictionnaire devient intéressante lorsque nous avons des sous-ensembles de données. 
# Par exemple, imagine que tu veux ranger des données alimentaire par groupes, par exemple des catégories d'aliments (légumes, viandes, féculents...). 
# Les ranger par numéro n'est pas le plus pratique, parce que tu vas avoir besoin d'un document faisant la correspondance entre les numéros pour te rappeler que 1 c'est pour les légumes, 2 pour les viandes, etc. 
# Avec un dictionnaire tu indiqueras directement "viandes" et python te renverra tous les aliments de la catégorie demandée.

food_fridge_dict = {
  "viandes": ["poulet", "bœuf", "porc"],
  "légumes": ["carottes", "brocoli", "épinards"],
  "féculents": ["riz", "pâtes", "pommes de terre"],
  "fruits": ["pommes", "bananes", "oranges"],
  "produits laitiers": ["lait", "fromage", "yaourt"]
}

food_fridge_list = [
  ["poulet", "bœuf", "porc"],
  ["carottes", "brocoli", "épinards"],
  ["riz", "pâtes", "pommes de terre"],
  ["pommes", "bananes", "oranges"],
  ["lait", "fromage", "yaourt"]
]

# Avec le dictionnaire, tu peux directement accéder à la catégorie "viandes" et obtenir la liste des viandes :
print()
print("Voici les viandes dans le frigo : ", food_fridge_dict["viandes"])
print()

# Avec la liste, tu dois te souvenir que les viandes sont à l'index 0, les légumes à l'index 1, etc. :
print("Voici les viandes dans le frigo : ", food_fridge_list[0])
print()

# Tout comme une liste, une dictionnaire est une boîte. 
# Il peut donc contenir tout ce qu'on veut.
# Il peut même avoir d'autres dictionnaires à l'intérieur de lui-même, ce qui est très pratique pour organiser des données complexes.
# La clé sera toujours alphanumérique.

house_and_food_dict = {
   "nourriture": {
       "viandes": ["poulet", "bœuf", "porc"],
       "légumes": ["carottes", "brocoli", "épinards"],
       "féculents": ["riz", "pâtes", "pommes de terre"],
       "fruits": ["pommes", "bananes", "oranges"],
       "produits laitiers": ["lait", "fromage", "yaourt"]
   },
   "mobilier": {
       "salon": ["canapé", "table basse", "télévision", "bar"],
       "cuisine": ["table", "chaises", "armoires"],
       "chambre": ["lit", "armoire", "commode"]
   }
}

# Comment accéder à la liste des légumes dans le dictionnaire "house_and_food_dict" ?
print()
print("Voici les légumes dans le frigo : ", house_and_food_dict["nourriture"]["légumes"])
print()

# Comment accéder à la liste des meubles de la cuisine dans le dictionnaire "house_and_food_dict" ?
print("Voici les meubles de la cuisine : ", house_and_food_dict["mobilier"]["cuisine"])
print()

# Comment accéder à l'élément "bar" dans le dictionnaire "house_and_food_dict" ?

print("Affichage de la valeur 'bar' : ", house_and_food_dict["mobilier"]["salon"][3])
print()


# Considérant un dictionnaire où chaque clé est associée à une liste de chaînes de caractères (strings) comme valeur, 
# écrivez un code pour récupérer tous les éléments de ces listes qui commencent par la lettre 'C'.

for i in house_and_food_dict.values():
    for v in i:
        print(v)

multi_group_dict = {
    "groupe1": ["Alice", "Bob", "Charlie", "Catherine"],
    "groupe2": ["David", "Eve", "Cindy", "Frank"],
    "groupe3": ["Grace", "Heidi", "Charlie", "Ivan", "Clélia"]
}

for i in multi_group_dict.values():
    for v in i:
        if v.startswith("C"):
            print("Voici la liste des personnes dont le nom commence par 'C' : ", v)

# autre solution

for key, values in multi_group_dict.items():
    for element in values:
        if element.startswith("C"):
            print("Voici la liste des personnes dont le nom commence par 'C' : ", element)

# autre solution

[v for values in multi_group_dict.values() for v in values if v.startswith("C")]
# Cette dernière solution utilise une compréhension de liste pour créer une nouvelle liste contenant uniquement les éléments 
# qui commencent par 'C' à partir des listes associées à chaque clé du dictionnaire multi_group_dict.


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