# Simplifier l'écriture d'une action en utilisant une fonction

# Examinonons le code suivant, qui travaille l'esthétique de sa sortie :

# for i_col in range(40):
#   print("*", end="")
# print()  

# nombre = float(input("Entrez un nombre : "))
# print("Le carré de ce nombre est :", nombre ** 2)

# for i_col in range(40):
#   print("*", end="")
# print()

# A la sortie de code, nous obtiendrons quelque chose comme ceci :
# ****************************************
# Entrez un nombre : 5.1251
# Le carré de ce nombre est : 26.265001
# ****************************************

# Nous pouvons simplifier l'écriture de ce code en utilisant une fonction pour afficher les étoiles. Voici comment nous pouvons le faire :

# def ligne_etoiles():
#   for i_col in range(40):
#     print("*", end="")
#   print()

# ligne_etoiles()
# nombre = float(input("Entrez un nombre : "))
# print("Le carré de ce nombre est :", nombre ** 2)
# ligne_etoiles()


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

# password = 4242

# enter_code = "Entrer le code :"

# again = "Encore une fois."

# bravo = "Bravo."

# def wait_password():
#   code_is_ok = False

#   while not code_is_ok:
#     print(enter_code)
#     code = int(input())
#     if code == password:
#       code_is_ok = True

# def check_password():
#   wait_password()
#   print(again)
#   wait_password()
#   print(bravo)

# check_password()

# other way to do it:

# password = 4242

# enter_code = "Entrez le code :"

# again = "Encore une fois."

# bravo = "Bravo."

# def wait_password():
#   code = 0 
#   while code != password:
#     print(enter_code)
#     code = int(input())

# def check_password():
#   wait_password()
#   print(again)
#   wait_password()
#   print(bravo)

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

# first_password = 4242
# second_password = 2121

# enter_code = "Entrez le code :"

# first_approval = "Premier code bon."

# bravo = "Bravo."

# def wait_password(password):
#   code = 0
#   while code != password:
#     print(enter_code)
#     code = int(input())

# def check_password():
#   wait_password(first_password)
#   print(first_approval)
#   wait_password(second_password)
#   print(bravo)

# check_password()

# other way to do it:

# first_password = 4242
# second_password = 2121

# enter_code = "Entrez le code :"

# first_approval = "Premier code bon."

# bravo = "Bravo."

# def wait_password(password, message):
#   code = 0
#   while code != password:
#     print(message)
#     code = int(input())

# def check_password():
#   wait_password(first_password, enter_code)
#   print(first_approval)
#   wait_password(second_password, enter_code)
#   print(bravo)

# check_password()

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

# ligne_caracteres("*")

def ligne_etoiles():
  ligne_caracteres("*") 

ligne_etoiles()

def ligne_tirets():
  ligne_caracteres("-")

ligne_tirets()

