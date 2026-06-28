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
Le mot de passe que vous choisissez est 4242. Écrivez un programme qui attend ce code une première fois, en le demandant de manière répétée par une ligne contenant « Entrez le code : », puis qui une fois ce code entré, affiche « Encore une fois. » et attend le code à nouveau, avant d'afficher « Bravo. » et de se terminer (vous trouverez sans doute cela plus clair avec l'exemple ci-dessous).

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

# def enter_code():
#   print("Entrez le code :", end="")

# def again():
#   print("Encore une fois.", end="")

# def bravo():
#   print("Bravo.", end="")

# def wait_password():
#   while True:
#     enter_code()
#     code = int(input())
#     if code == password:
#       return


# def check_password():
#   wait_password()
#   again()
#   print()
#   wait_password()
#   bravo()

# check_password()

# Other way to do it:

password = 4242 

def enter_code():
  print("Entrez le code :", end="")

def again():
  print("Encore une fois.", end="")

def bravo():
  print("Bravo.", end="")

def wait_password():
  attempt = 0
  while attempt != password:
    enter_code()
    print()
    attempt = int(input())

def check_password():
  wait_password()
  again()
  print()
  wait_password()
  bravo()

check_password()