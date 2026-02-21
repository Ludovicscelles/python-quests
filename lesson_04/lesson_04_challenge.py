# Challenge lesson_04

# Loop

# 1.1 - Fais une boucle qui renvoie les valeurs de 0 à 9.
# indice: Utilises la fonction range()

for i in range(0, 9):
  print(i)

# 1.2 - Fais une boucle qui renvoie les valeurs de 1 à 20.

for i in range(1, 20):
  print(i)

# 1.3 - Fais une boucle qui renvoie les nombres pairs entre 2 et 20 inclus.

for i in range(2, 21):
  print(i)

# 1.4 - Fais une boucle qui renvoie les valeurs de 10 à 1, donc dans l'ordre décroissant.

for i in range (10, 0, -1):
  print(i)

# 1.5 - Fais une boucle qui affiche 5 fois "Bonjour":

for i in range(5):
  print("Bonjour")

# 1.6 - Fais une boucle qui affiche "Bonjour", puis "aurevoir" 5 fois, comme dans l'exemple ci-dessous.

for i in range(5):
  print("Bonjour\nAurevoir")

# 1.7 - Fais une boucle qui affiche chaque lettre du mot "Blanquette", comme ceci:

for i in "Blanquette":
  print(i)

# 1.8 - Fais une boucle qui affiche en sortie, à chaque ligne, le numéro du tour de la boucle, comme ci-dessous.

for i in range(1, 10):
  print("C'est le tour numéro ",i)



# Loop sur les éléments d'une list

# 2.1 - Fais une boucle qui affiche chacun des éléments de la list ci-dessous.

cartoon = ['Babar', "Pingu", "oui-oui"]
for i in cartoon:
  print(i)

# 2.2 - Fais une boucle qui n'affiche que les éléments de la liste ci-dessous qui commencent par la lettre "B".

names = ["Ivan", "Geoffrey", "Benjamin", "Berthe", "Coline", "Achraf", "Géraldine", "Camille", "Benoît"]

for element in names:
  if element.startswith("B"):
    print(element)

# 2.3 - Fais une boucle qui n'affiche que les éléments de la liste ci-dessous qui sont supérieurs à 5.

number = [0, -3, 10, 6, 4, 5, -23, 12, 32]
for n in number:
  if n > 5:
    print(n)


# 2.4 - Fais une boucle qui n'affiches que les éléments de la liste ci-dessous qui sont supérieurs à 25 et inférieurs à 50 lorsqu'on les élève au carré:

number = [0, -3, 10, 6, 4, 5, -23, 12, 32, 7]
for n in number:
  if n > 25 and n**2 < 50:
    print(n)
    

