# Challenge lesson_03

# 1. Calcul du montant d'une remise
# Un commerçant accorde une remise de 5 % pour tout achat d’un montant compris entre 100 et 500 € et 8 % au-delà.
# Ecrivez un programme de calcul du montant de la remise sur un achat donné.
# Affichez le montant de la remise.

amount =float(input("Montant de la commande : " ))
reduction = 0.0
if amount < 100:
  reduction = 0.0
elif amount >= 100 and amount <= 500:
  reduction = amount * 0.05
else:
  reduction = amount * 0.08

print(f"La reduction de la commandes est de {reduction:.2f} €")


# 2. Savoir si trois entiers sont triés
# Ecrivez un programme faisant saisir trois entiers x, y, z à l’utilisateur, et lui indiquer si ces nombres sont dans l’ordre croissant (x <= y <= z).

x = int(input("Saisissez un nombre entier : "))
y = int(input("Saisissez un nombre entier : "))
z = int(input("Saisissez un nombre entier : "))
if x <= y and y <= z:
  print("Les nombres x, y et z sont dans l'ordre croissant")
else:
  print("Les nombres x, y et z ne sont pas dans l'ordre croissant")


# 3. Tri de trois réels
# Ecrivez un programme faisant saisir trois nombres réels x, y, z à l’utilisateur et qui les trie par ordre croissant (à la fin du # déroulement du programme x ≤ y ≤ z).
# Affichez x, y et z.

x = float(input("Saisissez un nombre réel : "))
y = float(input("Saisissez un nombre réel : "))
z = float(input("Saisissez un nombre réel : "))

if x > y:
  x, y = y, x
if y > z:
  y, z = z, y
if x > y:
  x, y = y, x

print(f"x = {x}, y = {y}, z = {z}")

# 4. Signe d'un produit
# Ecrivez un programme qui affiche le signe du produit de deux nombres réels sans calculer la valeur de ce produit. Par signe, on entend # positif, négatif ou nul.

a = float(input("Saisissez un nombre réel : "))
b = float(input("Saisissez un nombre réel : "))

if a == 0 or b == 0:
  print("Le signe du produit est nul.")
elif a * b > 0:
  print("Le signe du produit est positif.")
else:
  print("Le signe du produit est négatif.")