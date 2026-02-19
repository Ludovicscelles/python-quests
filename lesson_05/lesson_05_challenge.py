# Challenge lesson_05


# Mission 1: Commenter son code
# Une clé pour progresser rapidement en Python: Commenter le code.
# On ne te le répètera jamais assez, commente ton code.
# Cette bonne pratique va te rassurer, car tu comprends ainsi ce qu'il se passe à chaque ligne de code, sans louper d'étapes.

# "Rien ne sert de courir, il faut partir à point."

# C'est à ton tour de commenter le code ci-dessous.
# Pour t'entraîner, n'hésite pas à faire le calcul de tête, pour savoir combien de fois apparaîtront chaque mot.

une_macedoine = [] # Initialisation d'une liste vide "une_macedoine".

for nectarifaire in range(4, 120, 3): # Utilisation d'une boucle for pour itérer avec un pas de 3 sur les nombres de 4 à 119.
    if nectarifaire > 40:             # Condition : si la valeur dépasse 40,
        une_macedoine.append("carotte") # alors on ajoute deux légumes "carotte" et "flageolet" à la liste "une_macedoine" à chaque itération .
        une_macedoine.append("flageolet")

print()
print("une_macedoine =", une_macedoine) # Affichage de la liste "une_macedoine" après la boucle.


# Mission 2 : Débugger son code

# Tu as déjà du remarqué que quand tu débutes en Python, et que tu vois un code comme ci-dessus, ça donne des sueurs froides.
# En effet, on est rapidement perdu par rapport à ce qu'il se passe.
# Pas de panique ! C'est tout à fait normal.
# Connaître les objets et leurs différences, c'est une chose. Mais parvenir à comprendre ce qu'il se passe quand on code, c'en est une autre.

# Comme tu peux le voir ci-dessus, plusieurs print()ont été placés. C'est très utile pour comprendre ce qu'il se passe dans le code.
# Si tu utilises cette bonne pratique, ta progression dans la mâitrise de Python va considérablement augmenter !

# Ton objectif dans cette mission, c'est de savoir ce qui est contenu dans chacune des variables, après exécution du code ci-dessous.
# Pour y parvenir, tu as uniquement le droit de mettre des print()intermédiaires (c'est à dire entre les lignes), '
# 'en 'printant"(affichant)la ou les variables de ton choix. Pour cette mission, tu n'as pas le droit d'afficher les variables à la fin de la cellule, ou dans une autre cellule.

joga_bonito = []
joga_bonito_1 = []
compteur = 0

print()
for vvv in "Bonjour":
  print("variable vvv", vvv)

  for v in vvv:
    bonjour = "¿Hola qué tal amigos?"
    print("variable v", v)
    joga_bonito.append((v, bonjour))
    print("joga_bonito", joga_bonito)

  joga_bonito_1.append(v)
  print("joga_bonito_1 =", joga_bonito_1)

  compteur += len(bonjour)
  print("compteur =", compteur)
  print()


# Mission 3 : Calcul

# Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant: Tu dois combiner les variables avec des opérateurs mathématiques (*+-/) pour trouver le résultat 466.
# Tu assigneras le résultat à la variable answer.
# Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.

var_1 = 12
var_2 = 20
var_3 = 15
var_4 = 3
var_5 = 30

answer = (var_5 * var_3) + ((var_1 * var_4) - var_2)

print(answer)

# Mission 4 : Manipulation des objets et leur type

var_1 = 1
var_2 = "bouche"
var_3 = "bée"
var_4 = "la"
var_5 = "qu'"
var_6 = "de"
var_7 = "douche"
var_8 = "la"
var_9 = "boucherie."


words = [
    str(var_1),
    var_2,
    var_2,
    var_3,
    var_5 + str(var_1),
    var_2,
    var_2,
    var_8,
    var_2,
    var_6,
    var_7,
    var_6,
    var_8,
    var_9
]



phrase = " ".join(words)

print()
print(phrase)
print()

# Mission 5: Affectation parallèle

# En python, certains objets peuvent contenir d'autres objets.
# C'est le cas de l'objet de type tuple, qui peut contenir plusieurs éléments, qui sont eux-même des objets d'un certain type.
# C'est le cas ci-dessous, avec un tuple qui contient 3 élément: 1 int et 2 strings.

# Ton objectif est d'affecter chacune des valeurs contenues dans le tuple à des variables disctinctes. 
# Tu pourras ensuite répondre aux questions qui suivent, en indiquant simplement une variable par cellule de code.

a_tuple = (3, "Wild Code School", "Rose")

# Votre code ici

number_of_project = a_tuple[0]
school_name = a_tuple[1]
logo_color = a_tuple[2]

a_tuple = (3, "Wild Code School", "Rose")

# Quel est le nom de l'école ?
school_name
print(school_name)
print()

# Combien de projets sont à réaliser ?
number_of_project
print(number_of_project)
print()

# De quelle couleur est le logo de l'école ?
logo_color
print(logo_color)
print()

# Mission 6: Compteur

phrase = "Ton tonton tond un thon à Thonon."

# Votre code ici

count = phrase.count("on")


count
print(count)
print()

# Mission 7: Chaining


# Tu sais ce qu'est le "chaining" ?
# Concrètement, il s'agit d'enchaîner des méthodes les unes après les autres (en série) pour arriver à tes fins.
# Un peu comme un bon footballeur ferait pour marquer un but (passement de jambes, crochet, petit-pont, frappe et but !), tu vas devoir enchaîner les méthodes les unes après les autres pour atteindre ton objectif.
# Ton objectif, c'est d'appliquer plusieurs méthodes les unes à la suites des autres (chaining) pour obtenir la phrase suivante:
# Ah mais vous savez, je ne pense pas qu'il y ai de bonnes ou de mauvaises situations.
# Tu as le droit d'utiliser plusieurs fois la même méthode.

phrase = "Ah maIS vows SavUZ, je ge PUHSe Pas qw'il y Ait de BoggUS ow de MawVaiSUS siTwatIOHs."

# Votre code ici

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
print()






