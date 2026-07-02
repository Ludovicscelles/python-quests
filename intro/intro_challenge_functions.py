# Simplifier l'écriture d'une action en utilisant une fonction

# Examinonons le code suivant, qui travaille l'esthétique de sa sortie :

for i_col in range(40):
  print("*", end="")
print()  

nombre = float(input("Entrez un nombre : "))
print("Le carré de ce nombre est :", nombre ** 2)

for i_col in range(40):
  print("*", end="")
print()

# A la sortie de code, nous obtiendrons quelque chose comme ceci :
# ****************************************
# Entrez un nombre : 5.1251
# Le carré de ce nombre est : 26.265001
# ****************************************

# Nous pouvons simplifier l'écriture de ce code en utilisant une fonction pour afficher les étoiles. Voici comment nous pouvons le faire :

def ligne_etoiles():
  for i_col in range(40):
    print("*", end="")
  print()

ligne_etoiles()
nombre = float(input("Entrez un nombre : "))
print("Le carré de ce nombre est :", nombre ** 2)
ligne_etoiles()


""""

Code secret deux fois

Pour montrer aux jeunes Algoréens ce dont est capable votre robot, vous souhaitez écrire un programme qui demande deux fois le même mot de passe à son utilisateur.

Ce que doit faire votre programme :
Le mot de passe que vous choisissez est 4242. Écrivez un programme qui attend ce code une première fois, 
en le demandant de manière répétée par une ligne contenant « Entrez le code : », puis qui une fois ce code entré, affiche « Encore une fois. » 
et attend le code à nouveau, avant d'afficher « Bravo. » 
et de se terminer (vous trouverez sans doute cela plus clair avec l'exemple ci-dessous).

L'objectif de cet exercice est d'utiliser une fonction pour éviter de recopier deux fois les instructions qui permettent d'attendre le code 4242.

Exemple
entrée :

4241
4342
4242
2424
4242
sortie :

Entrez le code :
Entrez le code :
Entrez le code :
Encore une fois.
Entrez le code :
Entrez le code :
Bravo.



"""

password = 4242

enter_code = "Entrer le code :"

again = "Encore une fois."

bravo = "Bravo."

def wait_password():
  code_is_ok = False

  while not code_is_ok:
    print(enter_code)
    code = int(input())
    if code == password:
      code_is_ok = True

def check_password():
  wait_password()
  print(again)
  wait_password()
  print(bravo)

check_password()

# other way to do it:

password = 4242

enter_code = "Entrez le code :"

again = "Encore une fois."

bravo = "Bravo."

def wait_password():
  code = 0 
  while code != password:
    print(enter_code)
    code = int(input())

def check_password():
  wait_password()
  print(again)
  wait_password()
  print(bravo)

# check_password()


"""
Cette fois-ci, vous souhaitez montrer aux jeunes recrues un programme qui demande deux codes secrets différents.

Ce que doit faire votre programme :

Vous choisissez 2121 comme deuxième mot de passe. Écrivez un programme qui attend successivement les codes 4242 puis 2121, 
en affichant cette fois « Premier code bon. » entre les deux, comme montré dans l'exemple.

Ici, écrivez une et une seule fonction pour demander successivement les deux codes.

Exemple
entrée :

12
42345
4242
123
2121
sortie :

Entrez le code :
Entrez le code :
Entrez le code :
Premier code bon.
Entrez le code :
Entrez le code :
Bravo.


"""

first_password = 4242
second_password = 2121

enter_code = "Entrez le code :"

first_approval = "Premier code bon."

bravo = "Bravo."

def wait_password(password):
  code = 0
  while code != password:
    print(enter_code)
    code = int(input())

def check_password():
  wait_password(first_password)
  print(first_approval)
  wait_password(second_password)
  print(bravo)

check_password()

# other way to do it:

first_password = 4242
second_password = 2121

enter_code = "Entrez le code :"

first_approval = "Premier code bon."

bravo = "Bravo."

def wait_password(password, message):
  code = 0
  while code != password:
    print(message)
    code = int(input())

def check_password():
  wait_password(first_password, enter_code)
  print(first_approval)
  wait_password(second_password, enter_code)
  print(bravo)

check_password()

# Fonctions à un paramètre

# Nous venons de voir comment les fonctions permettent d'éviter de répéter exactement les mêmes instructions à plusieurs endroits d'un programme. 
# Il arrive aussi souvent que l'on répète les mêmes instructions, mais avec de légères différences d'une version à l'autre. 
# Supposons par exemple que nous souhaitions afficher une ligne d'étoiles au début et une ligne de tirets un peu plus loin. 
# Les instructions utilisées dans les deux cas seront identiques à un caractère près.

# Voici un exemple de code qui affiche une ligne d'étoiles, puis une ligne de tirets :

def ligne_caracteres(caractere):
  for i_col in range(40):
    print(caractere, end="")
  print()

ligne_caracteres("*")

def ligne_etoiles():
  ligne_caracteres("*") 

ligne_etoiles()

def ligne_tirets():
  ligne_caracteres("-")

ligne_tirets()


# Modifier une variable au sein d'une fonction

# Dans le cas où l'on souhaite modifier une variable au sein d'une fonction, 
# il est important de comprendre que les variables locales à la fonction ne modifient pas les variables globales.
# Si le paramètre d'une fonction est une variable globale, la valeur de cette variable ne sera pas modifiée par la fonction.

# Exemple :

def affiche_et_modifie(param):
  print("Debut de la fonction, param =", param)
  param = 68
  print("Fin de la fonction, param =", param)

variable = 42
print("Avant l'appel de la fonction, variable =", variable)
affiche_et_modifie(variable)
print("Après l'appel de la fonction, variable =", variable)


# Fonctions à plusieurs paramètres

# Il est possible de définir des fonctions qui prennent plusieurs paramètres.
# Dans l'exemple de la fonction ligne_caracteres, nous pourrions par exemple ajouter un paramètre qui permet de définir le nombre de caractères à afficher.
# Pour cela, il suffit d'ajouter un paramètre supplémentaire à la définition de la fonction, de l'utiliser dans le corps de la fonction 
# et de séparer ces deux paramètres par une virgule.

# Exemple :

def ligne_caracteres(caractere, nombre):
  for i_col in range(nombre):
    print(caractere, end="")
  print()

ligne_caracteres("*", 40)

ligne_caracteres("-", 20)


# Remarque : si l'on a défini que la fonction prenait deux paramètres, il est obligatoire de lui passer deux arguments lors de son appel.
# En Python, il est toutefois possible de rendre certains paramètres facultatifs en leur donnant une valeur par défaut dans la définition de la fonction.

# Exemple :

def ligne_caracteres(caractere = "*", nombre = 40):
  for i_col in range(nombre):
    print(caractere, end="")
  print()

ligne_caracteres()  # Affiche une ligne de 40 étoiles
ligne_caracteres("-", 20)  # Affiche une ligne de 20 tirets
ligne_caracteres("#")  # Affiche une ligne de 40 dièses
ligne_caracteres("=", 10)  # Affiche une ligne de 10 signes égal


"""
Dentelle

Vos spectateurs aiment beaucoup la dentelle comportant une ligne de « X », une ligne de dièses « # » et une ligne de « i ». 
Ils voudraient que vous écriviez un programme pour leur en fournir la quantité qu'ils désirent.

Ce que doit faire votre programme :
Votre programme doit lire la longueur de la dentelle, puis l'afficher sous la forme de trois lignes remplies respectivement de « X », de « # » et de « i ».

Exemple
entrée :

5
sortie :

XXXXX
#####
iiiii


"""

length = int(input())

letter_x = "X"
sharp = "#"
letter_i = "i"

def lace_line(sign, length):
  for col_i in range(length):
    print(sign, end="")
  print()

def lace(length):
  lace_line(letter_x, length)
  lace_line(sharp, length)
  lace_line(letter_i, length)

lace(length)

""""
À présent, vos spectateurs ont envie que votre robot imprime un motif sur une feuille rectangulaire de n'importe quelle taille, car cela leur sert pour des jeux de géométrie.

Ce que doit faire votre programme :
Votre programme doit lire le nombre de lignes et de colonnes de la feuille, puis le motif à afficher sous la forme d'un caractère. 
Il doit alors afficher le motif de sorte qu'il remplisse chaque cellule de la feuille.

Exemples
Exemple 1
entrée :

4
9
F
sortie :

FFFFFFFFF
FFFFFFFFF
FFFFFFFFF
FFFFFFFFF
Exemple 2
entrée :

8
3
P
sortie :

PPP
PPP
PPP
PPP
PPP
PPP
PPP
PPP


"""

line_number = int(input())
col_number = int(input())
pattern = input()

def pattern_line(pattern, col_number):
  print(pattern * col_number)

def pattern_sheet(line_number, col_number, pattern):
  for line in range(line_number):
    pattern_line(pattern, col_number)

pattern_sheet(line_number, col_number, pattern)

# Other way to do it:

line_number = int(input())
col_number = int(input())
pattern = input()

def pattern_sheet(line_number, col_number, pattern):
  for line in range(line_number):
    for col in range(col_number):
      print(pattern, end="")
    print()

pattern_sheet(line_number, col_number, pattern)

# Valeur de retour d'une fonction

# Il est possible de faire en sorte qu'une fonction retourne une valeur, c'est-à-dire qu'elle produise un résultat qui pourra être utilisé par le programme appelant.

# Exemple :

def valeur_absolue(nombre):
  if nombre < 0:
    val_absolue = -nombre
  else:
    val_absolue = nombre
  return val_absolue

variable = -42
print("La valeur absolue de", variable, "est", valeur_absolue(variable))

# Le mot-clé return permet de renvoyer une valeur à l'endroit où la fonction a été appelée.

# Il est possible d'utiliser plusieurs fois le mot-clé return dans une fonction, mais dès qu'un return est exécuté, la fonction s'arrête et retourne la valeur indiquée.


def valeur_absolue(nombre):
  if nombre < 0:
    return -nombre
  else:
    return nombre
  
variable = -42
print("La valeur absolue de", variable, "est", valeur_absolue(variable))

"""
Vos apprentis ont remarqué dans votre manuel une fonction min, qui prend deux valeurs en paramètre et fournit la plus petite des deux. 
Ils se demandent comment est codée cette fonction.

Ce que doit faire votre programme :
Écrivez une fonction nommée min2, qui prend deux entiers en paramètres et retourne le plus petit. 
Pour démontrer l'utilisation de cette fonction, vous lirez 10 entiers sur l'entrée, utiliserez votre fonction pour conserver uniquement le plus petit des 10, puis vous l'afficherez à la fin.

Exemple
entrée :

4
3
6
2
6
8
9
8
5
4
sortie :

2


"""

def min2(a, b):
  if a < b:
    return a
  return b
  
number_of_digits = 10

for i in range(number_of_digits):
  digit = int(input())
  if i == 0:
    min_digit = digit
  else:
    min_digit = min2(min_digit, digit)

print(min_digit)

# Other way to do it:

def min2(a, b):
  if a < b:
    return a
  return b

numbers_of_digits = 10

min_digit = int(input())

for i in range(numbers_of_digits - 1):
  digit = int(input())
  min_digit = min2(min_digit, digit)

print(min_digit)

"""
Phénomène numérique

Les jeunes attirent à présent votre attention sur des suites de nombres entiers qui semblent avoir certaines similitudes, surtout sur leurs terminaisons.

Dans cette suite, le nombre qui suit un nombre terme est :

si terme est pair, terme ÷ 2 ;
sinon, terme × 3 + 1.
Vos compagnons ont remarqué que, quel que soit le nombre dont on part, en allant d'un terme à l'autre en suivant ces propriétés, on finit toujours par tomber sur le nombre 1.
Ainsi, ils souhaitent que leur écriviez une fonction qui, pour un terme, renvoie le terme suivant dans la suite.

Ce que doit faire votre programme :
Votre programme doit afficher les termes de la suite qui succèdent à celui fourni sur l'entrée, séparés par des espaces, jusqu'à ce que le nombre 1 soit atteint.

Important : vous devez utiliser une fonction qui prend un terme en paramètre, et retourne le suivant.

Exemple
entrée :

7
sortie :

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1


"""

number = int(input())

def terms_suit(number):
  result = number

  while result != 1:
    if result % 2 == 0:
      result = result // 2
    else:
      result = result * 3 + 1
    
    print(result, end=" ")

terms_suit(number)

# Other way to do it:

def next_term(term):
  if term % 2 == 0:
    return term // 2
  else:
    return term * 3 + 1
  
term = int(input())

while term != 1:
  term = next_term(term)
  print(term, end=" ")
print()


"""
Distance euclidienneEntraînement
Imprimer	
SujetRésoudreConseilsActivitéCorrection
Sur les feuilles à motifs que vous leur avez imprimées tout à l'heure, les jeunes gens souhaiteraient calculer la distance entre deux motifs, 
ce qui ce fait facilement si l'on perçoit la feuille comme un repère orthonormé.

Ce que doit faire votre programme :
Écrivez une fonction qui prend en paramètre les coordonnées (𝑥1,𝑦1)
 et (𝑥2,𝑦2)
 de deux points et retourne la distance euclidienne entre ces deux points. 
 On rappelle que la distance euclidienne entre deux points est égale à :

(𝑥2−𝑥1)2+(𝑦2−𝑦1)2‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√
Utilisez ensuite cette fonction dans un programme qui lit quatre nombres décimaux 𝑥1
, 𝑦1
, 𝑥2
 et 𝑦2
 tapés au clavier, puis affiche la distance entre les deux points correspondants.

On pourra utiliser la fonction mathématique sqrt(x) qui retourne la racine carrée du paramètre x et qui s'importe avec cette ligne :

from math import *
Exemple
entrée :

22.5
46.8
4.25
7.22
sortie :

43.584847


"""

from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def euclidean_distance(x1, y1, x2, y2):
  distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
  return distance

print(euclidean_distance(x1, y1, x2, y2))


"""
Vos spectateurs veulent davantage de dessins.

Ce que doit faire votre programme :
Écrivez un programme qui affiche une ligne de « X », un rectangle de « # », et un triangle de « @ ». 
Les deux formes doivent être creuses (remplies avec des espaces).

L'entrée comporte quatre entiers, un par ligne :

le nombre de « X » de la ligne à afficher ;
le nombre de lignes du rectangle de « # » ;
le nombre de colonnes du rectangle ;
le nombre de lignes du triangle de « @ ».
Vous devez afficher les trois formes successivement, avec une ligne blanche entre chaque forme, comme le montre l'exemple.

Votre objectif doit être d'obtenir le code source le plus simple et clair possible, en le décomposant en fonctions.

Exemple
entrée :

15
5
12
6
sortie :

XXXXXXXXXXXXXXX

############
#          #
#          #
#          #
############

@
@@
@ @
@  @
@   @
@@@@@@
Commentaires
Attention : le nombre de lignes ou de colonnes peut être égal à 1.


"""
# # reuse functions :

space = " "

def complete_line(sign, sign_number):
  return sign * sign_number

def hollow_line(sign, space, length):
  return(sign + (space * length) + sign)

# # x_lines :

x_number = int(input())
x_sign = "X"

def x_line(x_sign, x_number):
  print(complete_line(x_sign, x_number))

# # sharp_rectangle :

sharp_line_number = int(input())
sharp_col_number = int(input())
sharp_sign = "#"

def complete_sharp_line(sharp_sign, sharp_col_number):
  return (complete_line(sharp_sign, sharp_col_number))

def hollow_sharp_line(sharp_sign, space, sharp_col_number):
  if sharp_col_number == 1:
    return sharp_sign
  else:
    return(hollow_line(sharp_sign, space, (sharp_col_number - 2)))
  
def sharp_rectangle(sharp_line_number):
  full_line = complete_sharp_line(sharp_sign, sharp_col_number)
  if sharp_line_number == 1:
    print(full_line)
  else:
    print(full_line)
    for _ in range(1, sharp_line_number -1):
      next_lines = hollow_sharp_line(sharp_sign, space, sharp_col_number)
      print(next_lines)
    print(full_line)

# # @_triangle

arobase_line_number = int(input())
arobase_sign = "@"

def complete_arobase_line(arobase_sign, arobase_line_number):
  return complete_line(arobase_sign, arobase_line_number)

def hollow_arobase_line(arobase_sign, space, i):
    return (hollow_line(arobase_sign, space, (i - 1)))

def arobase_triangle(arobase_line_number):
  for i in range(arobase_line_number):
    if i == 0:
      print(arobase_sign)
    elif i == arobase_line_number - 1:
      print(complete_arobase_line(arobase_sign, arobase_line_number))
    
    else:
      print(hollow_arobase_line(arobase_sign, space, i))

# # global function 

def picture(x_line, sharp_rectangle, arobase_triangle):
  x_line(x_sign, x_number)
  print()
  sharp_rectangle(sharp_line_number)
  print()
  arobase_triangle(arobase_line_number)


picture(x_line, sharp_rectangle, arobase_triangle)

"""
Convertisseur d'unités

Ce que doit faire votre programme :
Écrivez un programme qui convertit des valeurs du système métrique en valeurs du système de mesure américain. 
On fournit des mesures à votre programme, en mètres, grammes ou degrés Celsius et vous devez les convertir respectivement en pieds, livres et degrés Fahrenheit.

Voici les règles de conversion à utiliser :

1 pied = 0,3048 mètres ;
1 gramme = 0,002205 livres ;
température en degrés Fahrenheit = 32 + 1,8 × température en degrés Celsius.
On vous donne sur la première ligne le nombre de conversions à effectuer, puis sur les lignes suivantes la valeur à convertir, et son unité : m, g ou c (avec une espace entre les deux).

Affichez en sortie les valeurs converties, suivies d'une espace et de leur unité : p, l ou f.

Il n'est en fait pas judicieux d'écrire des fonctions pour résoudre cet exercice : le mieux est de définir des constantes. 
Vous pouvez aussi profiter de cet exercice pour expérimenter l'instruction « selon », switch dans certains langages.

Exemple
entrée :

4
12.3 m
1245.243 g
37.2 c
23 g
sortie :

40.354331 p
2.745761 l
98.960000 f
0.050715 l
Commentaires
L'entrée indique qu'il y a quatre valeurs à convertir. 
La première est 12,3 mètres, ce qui, une fois converti, donne approximativement 40,354331 pieds. 
La deuxième est 1245,243 grammes, soit environ 2,745761 livres, la troisième est 37,2 degrés Celsius, soit 98,96 degrés Farenheit, et la quatrième est 23 grammes, soit 0,050715 livres.


"""

conversion_number = int(input())

meter_to_feet = 0.3048
gram_to_pound = 0.002205

def celsius_to_fahrenheit(celsius):
  return 32 + 1.8 * celsius

for _ in range(conversion_number):
  num, unit = input().split()
  num = float(num)
  if unit == "m":
    print(f"{num / meter_to_feet} p")
  elif unit == "g":
    print(f"{num * gram_to_pound} l")
  elif unit == "c":
    print(f"{celsius_to_fahrenheit(num)} f")
  else:
    print("Error number or unit")
  

  

