# Simple enregistrement

# Lorsque l'on a beaucoup de données, il peut s'avérer utile de les regrouper sous un seul nom.
# Pour cela, on peut créer une classe qui va contenir toutes les informations que l'on souhaite regrouper.
# Une classe est un modèle (ou un type) qui permet de définir des objets. 
# Ces objets peuvent contenir des données (appelées attributs) et des fonctions (appelées méthodes) qui manipulent ces données.
# Imaginons que l'on ait de nombreux dessins de rectangle à gérer ; on souhaiterait alors pouvoir regrouper ensemble leur nombre de lignes, ainsi que le caractère de remplissage.

# Exemple :

class dessin_rectangle:
    pass
# Le mot pass signifie que la classe ne contient rien pour l'instant. 
# C'est un "placeholder" qui permet de définir la classe sans erreur.
# Maintenant, on peut créer des instances de cette classe et les stocker dans des variables. 

rect_long = dessin_rectangle()
rect_long.nb_lignes = 3
rect_long.nb_colonnes = 12
rect_long.caractere_remplissage = "*"

rect_haut = dessin_rectangle()
rect_haut.nb_lignes = 8
rect_haut.nb_colonnes = 2
rect_haut.caractere_remplissage = "#"

rect_gros = dessin_rectangle()
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

rect_x = dessin_rectangle()
rect_x.nb_lignes = 5
rect_x.nb_colonnes = 5
rect_x.caractere_remplissage = "x"
copie = rect_x

# Attention, il ne s'agit pas d'une copie indépendante, mais d'une référence vers le même objet.
# Ainsi, si l'on modifie un attribut de l'un, l'autre sera également modifié.

# C'est l'appel dessin_rectangle() qui crée un nouvel objet (une nouvelle instance). 
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

# On peut également créer une nouvelle instance de la classe dessin_rectangle et lui affecter les mêmes attributs que l'instance rect_x.

#. Méthode 

# Une méthode est une fonction qui est définie à l'intérieur d'une classe et qui agit sur les instances de cette classe.
# Une méthode est définie comme une fonction normale, mais elle prend toujours au moins un paramètre : self.
# Le paramètre self fait référence à l'instance de la classe sur laquelle la méthode est appelée.

# Exemple :

class draw_rectangle:
    def dessiner_rectangle(self):
        for i_ligne in range(self.nb_lignes):
            for i_colonne in range(self.nb_colonnes):
                print(self.caractere_remplissage, end="")
            print()

# On peut maintenant créer une instance de la classe draw_rectangle et lui affecter des attributs, puis appeler la méthode dessiner_rectangle() sur cette instance.

# Exemple :

rect_long = draw_rectangle()
rect_long.nb_lignes = 3
rect_long.nb_colonnes = 12
rect_long.caractere_remplissage = "*"

print()
print("Dessin du rectangle rect_long :")
rect_long.dessiner_rectangle()

