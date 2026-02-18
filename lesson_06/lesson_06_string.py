# string

# Une chaîne de caractères est une séquence de caractères. 
# En Python, les chaînes de caractères sont définies entre guillemets simples (' ') ou doubles (" ").
str_1 = "Salut wilder !"
str_2 = 'Salut wilder !'
print(str_1)
print(str_2)

# Les chaînes de caractères sont immuables, c'est à dire qu'on ne peut pas les modifier une fois qu'elles sont créées.
# Si on veut modifier une chaîne de caractères, il faut en créer une nouvelle.
str_1 = "Salut wilder !"
str_1 = str_1.replace("Salut", "Hello") # On remplace "Salut" par "Hello" dans la chaîne str_1 et on assigne le résultat à str
print(str_1)
print(str_2)

# Les chaînes de caractères sont des objets, et comme tous les objets, elles ont des méthodes.

# Selectionner les charactères d'une chaîne de caractères

# Les indices commencent à 0, c'est à dire que le premier caractère d'une chaîne de caractères a l'indice 0, le deuxième caractère a l'indice 1, etc.
s = "Fudge"
print(s[0]) # Affiche le premier caractère de la chaîne
print(s[1]) # Affiche le deuxième caractère de la chaîne
print(s[2]) # Affiche le troisième caractère de la chaîne
print(s[-1]) # Affiche le dernier caractère de la chaîne
print(s[-2]) # Affiche l'avant-dernier caractère de la chaîne
print()

# Sélectionner avec des slices

print(s[0:3]) # Affiche les caractères de la position 0 à 2 (3 n'est pas inclus)
print(s[1:4]) # Affiche les caractères de la position 1 à 3 (4 n'est pas inclus)
print(s[:3]) # Affiche les caractères de la position 0 à 2 (3 n'est pas inclus)
print(s[2:]) # Affiche les caractères de la position 2 à la fin de la chaîne
print(s[:]) # Affiche tous les caractères de la chaîne


print()

string = "Ludovic Scelles"
print(string[0])
print(string[2])
print(string[-1])
print(string[0:2])
print(string[2:5])
print(string[0:4])
print(string[:4])
print(string[3:])
print(string[:]) # Affiche tous les caractères de la chaîne
print(string[1::2]) # Affiche les caractères de la position 1 à la fin de la chaîne, en sautant un caractère sur deux (1, 3, 5, etc.)
print()

# Les méthodes de chaînes de caractères

# Les méthodes de chaînes de caractères sont des fonctions qui sont associées à un objet chaîne de caractères.
# Elles permettent de manipuler les chaînes de caractères de différentes manières.
# Par exemple, la méthode replace() permet de remplacer une partie d'une chaîne de caractères par une autre partie.
word = "bonjour"
word = word.replace("b", "m")
print(word)
print()

# La méthode upper() permet de convertir une chaîne de caractères en majuscules.
word = "bonjour"
word = word.upper()
print(word)
print()

# La méthode lower() permet de convertir une chaîne de caractères en minuscules.
word = "BONJOUR"
word = word.lower()
print(word)
print()


# id() est une fonction qui permet de connaître l'identifiant d'un objet en mémoire.
id_word = id(word)
print(id_word)
print()

id_string = id(string)
print(id_string)
print()

# Comme les chaînes de caractères sont immuables, lorsque nous modifions une chaîne de caractères, nous créons en réalité une nouvelle chaîne de caractères en mémoire, et l'identifiant de la variable qui contient la chaîne de caractères change.
word = word.replace("m", "b")
id_word = id(word)
print(id_word)
print()

# On peut créer une chaine de caractères vide en utilisant des guillemets simples ou doubles.
phrase = ""


# On peut concaténer des chaînes de caractères en utilisant l'opérateur +.
a = "aze"
b = "rty"
c = ""

ab = a + b
ac = a + c
print(ab)
print(ac)
print()
