# Simple enregistrement

# Lorsque l'on a beaucoup de données, il peut s'avérer utile de les regrouper sous un seul nom.
# Pour cela, on peut créer une classe qui va contenir toutes les informations que l'on souhaite regrouper.
# Une classe est un modèle (ou un type) qui permet de définir des objets. 
# Ces objets peuvent contenir des données (appelées attributs) et des fonctions (appelées méthodes) qui manipulent ces données.
# Imaginons que l'on ait de nombreux dessins de rectangle à gérer ; on souhaiterait alors pouvoir regrouper ensemble leur nombre de lignes, ainsi que le caractère de remplissage.

# Exemple :

class DessinRectangle:
    pass
# Le mot pass signifie que la classe ne contient rien pour l'instant. 
# C'est un "placeholder" qui permet de définir la classe sans erreur.
# Maintenant, on peut créer des instances de cette classe et les stocker dans des variables. 

rect_long = DessinRectangle()
rect_long.nb_lignes = 3
rect_long.nb_colonnes = 12
rect_long.caractere_remplissage = "*"

rect_haut = DessinRectangle()
rect_haut.nb_lignes = 8
rect_haut.nb_colonnes = 2
rect_haut.caractere_remplissage = "#"

rect_gros = DessinRectangle()
rect_gros.nb_lignes = 10
rect_gros.nb_colonnes = 15
rect_gros.caractere_remplissage = "o"

# Dans la suite, on utilise l'opérateur point (.) pour accéder aux variables de chaque instance. 
# En Python, il est possible de créer des attributs directement sur une instance en utilisant le point (.)
# Les attributs fonctionnent comme des variables, mais sont attachés à une instance particulière de la classe.
# Plutôt que d'avoir trois variables indépendantes (nb_lignes, nb_colonnes, caractere_remplissage) pour chaque rectangle, on les regroupe dans un seul objet. 
# Cela permet de manipuler plus facilement plusieurs rectangles et d'écrire des fonctions qui prennent un rectangle en paramètre.

# Exemple d'utilisation :

def dessiner_rectangle(rectangle):
    for i_ligne in range(rectangle.nb_lignes):
        for i_colonne in range(rectangle.nb_colonnes):
            print(rectangle.caractere_remplissage, end="")
        print()

dessiner_rectangle(rect_long)
dessiner_rectangle(rect_haut)
dessiner_rectangle(rect_gros)

# Affectations entre instances

# On peut également affecter une instance à une autre variable.

# Exemple :

rect_x = DessinRectangle()
rect_x.nb_lignes = 5
rect_x.nb_colonnes = 5
rect_x.caractere_remplissage = "x"
copie = rect_x

# Attention, il ne s'agit pas d'une copie indépendante, mais d'une référence vers le même objet.
# Ainsi, si l'on modifie un attribut de l'un, l'autre sera également modifié.

# C'est l'appel DessinRectangle() qui crée un nouvel objet (une nouvelle instance). 
# Les variables (rect_long, rect_x, etc.) contiennent une référence vers cet objet.

# exemple :

copie.nb_lignes = 10
copie.nb_colonnes = 10
copie.caractere_remplissage = "z"
# copie et rect_x pointent vers le même objet, donc les modifications sont visibles depuis les deux variables.

copie.color = "red"
# On peut également ajouter de nouveaux attributs à un objet existant.

def dessiner_color_rectangle(rectangle):
    color = getattr(rectangle, "color", None)

    for i_ligne in range(rectangle.nb_lignes):
        for i_colonne in range(rectangle.nb_colonnes):
            if color == "red":
                print("\033[91m" + rectangle.caractere_remplissage + "\033[0m", end="")
            elif color == "blue":
                print("\033[94m" + rectangle.caractere_remplissage + "\033[0m", end="")
            elif color == "green":
                print("\033[92m" + rectangle.caractere_remplissage + "\033[0m", end="")
            else:
                print(rectangle.caractere_remplissage, end="")
        print()

dessiner_color_rectangle(rect_x)
dessiner_color_rectangle(copie)
rect_x.color = "blue"

dessiner_color_rectangle(copie)

copie.color = "green"
dessiner_color_rectangle(rect_x)

# On peut également créer une nouvelle instance de la classe DessinRectangle et lui affecter les mêmes attributs que l'instance rect_x.

#. Méthode 

# Une méthode est une fonction qui est définie à l'intérieur d'une classe et qui agit sur les instances de cette classe.
# Une méthode est définie comme une fonction normale, mais elle prend toujours au moins un paramètre : self.
# Le paramètre self fait référence à l'instance de la classe sur laquelle la méthode est appelée.

# Exemple :

class drawRectangle:
    def dessiner_rectangle(self):
        for i_ligne in range(self.nb_lignes):
            for i_colonne in range(self.nb_colonnes):
                print(self.caractere_remplissage, end="")
            print()

# On peut maintenant créer une instance de la classe drawRectangle et lui affecter des attributs, puis appeler la méthode dessiner_rectangle() sur cette instance.

# Exemple :

rect_long = drawRectangle()
rect_long.nb_lignes = 3
rect_long.nb_colonnes = 12
rect_long.caractere_remplissage = "*"

print()
print("Dessin du rectangle rect_long :")
rect_long.dessiner_rectangle()

"""
Exercice 1 – Créer une classe simple

Créer une classe personne.

Créer ensuite deux instances :

Alice, 25 ans
Bob, 42 ans

Chaque personne possède les attributs :

nom
age

Écrire une fonction afficher_personne(personne) qui affiche :

Nom : Alice
Âge : 25 ans

"""

class Person:
    pass

alice = Person()
alice.name = "Alice"
alice.age = 25

bob = Person()
bob.name = "Bob"
bob.age = 42

def display_identity(person):
    print(f"Nom : {person.name}")
    print(f"Âge : {person.age} ans")

display_identity(alice)
print()
display_identity(bob)

"""
Exercice 2 – Modifier une instance

On reprend la classe personne.

Créer une personne :

nom = "Julie"
age = 18

Puis modifier son âge pour qu'il vaille 19.

Afficher ensuite les nouvelles informations.

"""

julie = Person()
julie.name = "Julie"
julie.age = 18

print()
print("Avant la modification :")
display_identity(julie)

julie.age = 19

print()
print("Après la modification :")
display_identity(julie)

"""
Exercice 3 – Deux variables pour un même objet

Créer une instance :

chat = animal()
chat.nom = "Minou"
chat.age = 2

Puis écrire :

copie = chat

Modifier ensuite :

copie.age = 5

Afficher l'âge de :

chat
copie

Question :

Pourquoi les deux âges sont-ils identiques ?


"""
class Animal:
    pass

chat = Animal()
chat.name = "Minou"
chat.age = 2

chat_2 = chat

chat_2.age = 5 

print()
print(chat.age)
print(chat_2.age)

# Les deux âges sont identiques car les deux variables chat et chat_2 font référence à la même instance de la classe Animal.


"""
Exercice 4 – Ajouter un nouvel attribut

Créer une classe voiture.

Créer une voiture :

marque = "Renault"
modele = "Clio"

et afficher :

Ma voiture est une Clio de la marque Renault.

Puis ajouter un nouvel attribut :

couleur = "Rouge"

Afficher ensuite :

Ma voiture est une Clio de la marque Renault. Elle est de couleur Rouge.


"""

class Car:
    pass

my_car = Car()
my_car.brand = "Renault" 
my_car.model = "Clio"

print()
print(f"Ma voiture est une {my_car.model} de la marque {my_car.brand}")
print()

my_car.color = "Rouge"

print()
print(f"Ma voiture est une {my_car.model} de la marque {my_car.brand}. Elle est de couleur {my_car.color}.")
print()

"""
Exercice 5 – Écrire une méthode

Créer une classe chien.

Chaque chien possède :

nom
age

Ajouter une méthode :

def presenter(self):

qui affiche :

Je m'appelle Rex et j'ai 4 ans.

Créer ensuite un chien et appeler la méthode.

"""

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Je m'appelle {self.name} et j'ai {self.age} ans.")

rex = Dog("Rex", 4)
rex.introduce()

plutot = Dog("Plutôt", 6)
plutot.introduce()


"""
Exercice 6 – Dessiner un carré

Créer une classe carre.

Chaque carré possède :

taille
caractere

Ajouter une méthode dessiner() qui affiche un carré.

Exemple :

taille = 4
caractere = "#"

Affiche :

####
####
####
####

"""

class DrawSquare:

    def __init__(self, size, character):
        self.size = size
        self.character = character

    def draw_square(self):
        for i_line in range(self.size):
            for i_col in range(self.size):
                print(self.character, end="")
            print()


sharp_square = DrawSquare(4, "#")

print()
sharp_square.draw_square()
print()


"""
Exercice 7 – Plusieurs objets

Créer trois rectangles.

Chaque rectangle possède :

nb_lignes
nb_colonnes
caractere

Ajouter une méthode dessiner().

Dessiner ensuite les trois rectangles.

"""

class Rectangle:

    def __init__(self, rows, cols, character):
        self.rows = rows
        self.cols = cols
        self.character = character

    def draw(self):
        for i_line in range(self.rows):
            for i_col in range(self.cols):
                print(self.character, end="")
            print()

    
arobase_rectangle = Rectangle(5, 10, "@")
euro_rectangle = Rectangle(8, 4, "€")
dollar_rectangle = Rectangle(20, 8, "$")

print()
arobase_rectangle.draw()
print()
euro_rectangle.draw()
print()
dollar_rectangle.draw()
print()