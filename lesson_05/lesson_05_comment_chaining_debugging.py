# Commentaires Chaining et Debugging 

# Chaining

# Voici ci-dessous une liste de chansons d'un album des Enfoirés, "Bon anniversaire les Enfoirés" sortie en 2014.
songs = ['attention au départ', 'qu\'est-ce qu\'on fout à strasbourg', 
          'plaisir d\'amour', 'à quoi ça sert l\'amour', 'seras-tu là', ]

# On fait du chaining et on attribue le résultat à une variable result.
# On veut que le résultat soit une liste de mots, avec les premières lettres en majuscules.
result = " ".join(songs).title().split()

print(result)



# Voici une phrase qui a été mal écrite, avec des majuscules et des fautes d'orthographe.
# En utilisant du chaining, corrige la phrase et affiche le résultat.
phrase = "Ah maIS vows SavUZ, je ge PUHSe Pas qw'il y Ait de BoggUS ow de MawVaiSUS siTwatIOHs."

phrase = phrase.lower()
phrase = phrase.replace("savuz", "savez")
phrase = phrase.replace("vows", "vous")
phrase = phrase.replace("ge", "ne")
phrase = phrase.replace("qw", "qu")
phrase = phrase.replace("boggus", "bonnes")
phrase = phrase.replace("puhse", "pense")
phrase = phrase.replace("ow", "ou")
phrase = phrase.replace("mawvaisus", "mauvaises")
phrase = phrase.replace("sitwatiohs", "situation")
phrase = phrase.capitalize()

print()
print(phrase)

# Debugging

# Implement print at different stages of the code to understand what is happening 
# Initialisation de deux listes vides et d'un compteur à zéro
joga_bonito = []
joga_bonito_1 = []
compteur = 0

# On itère sur chaque caractère de la chaîne "Bonjour"
for vvv in "Bonjour":
  # Affichage de la variable vvv à chaque itération
  print("variable vvv", vvv) 

  # On itère sur le caractère contenu dans la variable vvv (une seule lettre)
  for v in vvv:
    # On crée une variable bonjour contenant toujours la même chaîne
    bonjour = "¿Hola qué tal amigos?"
    # Affichage de la variable v à chaque itération
    print("variable v", v)
    # On ajoute un tuple contenant v et bonjour à la liste joga_bonito
    joga_bonito.append((v, bonjour))
    # Affichage de la liste joga_bonito à chaque itération
    print("joga_bonito", joga_bonito)

# Après la boucle interne, on ajoute la variable v (la lettre courante) à la liste joga_bonito_1
  joga_bonito_1.append(v)
  print("joga_bonito_1 =", joga_bonito_1)
 
# On ajoute la longueur de la variable bonjour au compteur de chaque itération de la boucle externe
  compteur += len(bonjour)
  print("compteur =", compteur)



