# Challenge lesson_01

# 1. Les variables

# 1.1 Dans les cellules de code ci-dessous, quel est, pour chaque cellule, le type de chaque variable ?

count = 5
# C'est un integer (int).

greeting = "Hello World"
# C'est une string (str).

price = 2.5
# C'est un float (float).

is_active = True
# C'est un booléen.

# Convertissez la variable `count` en float.
count = 5
count_float = float(count)
print(count)
print(count_float)

# Convertissez la variable price en int

price = 5.4
price_int = int(price)
print(price)
print(price_int)

# Trouvez le moyen d'arrondir la variable `temperature`.

temperature = 5.3
temperature_round = round(temperature)
print(temperature_round)

# Ci-dessous, est-ce que height est un `int` ?

height = 6.0
# Non c'est un float


# 2. Les entrées/sorties

# Affichez le message suivant : "Hello world".

message = "Hello world."
print(message)

# Demandez à l'utilisateur s'il fait beau aujourd'hui.

weather = input("Est-ce qu'il fait beau aujourd'hui ?")

# 3. Tout ensemble !
# Maintenant tu vas combiner tout ce que tu as appris jusqu'à présent !

# 3.1 Première interaction avec l'utilisateur
# Réalisez les étapes suivantes dans l'ordre :

# Demande à l'utilisateur son age et stocke-le dans une variable de type ìnt.
# Vérifie le type de la variable.
# Affiche l'âge de l'utilisateur.

age = int(input("Quel est votre age ?"))
print(type(age))
print("Votre age est de " + str(age) + " ans.")

# 3.2 Inversion de deux variables
# Réalisez les étapes suivantes dans l'ordre :

# Demande à l'utilisateur de rentrer deux valeurs et stocke-les dans deux variables différentes (par exemple x et y).
# Effectue l'échange des valeurs entre ces deux variables.
# Affiche la valeur des deux variables.

ville1 = input("Quelle ville avez-vous visité cet été ?")
ville2 = input("Quelle autre ville avez-vous visité cet été ?")
ville1, ville2 = ville2, ville1
print("Cet été, j'ai visité " + ville2 + " et " + ville1 + "!")