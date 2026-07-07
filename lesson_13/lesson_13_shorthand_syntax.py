# Avec Python, il est possible d'utiliser une syntaxe abrégée pour certaines opérations courantes. 
# C'est souvent plus élégant (mais pas toujours plus lisible !).

# Exemple pour une fonction :

def square(number):
    return number ** 2

print(square(5)) # affiche 25

# On peut également utiliser une syntaxe abrégée pour les fonctions, appelée "lambda" (ou fonction anonyme).

square_short = lambda number: number ** 2

print(square_short(5)) # affiche également 25


# lambda est l'équivalent d'une fonction définie avec def, mais elle est plus concise.
# lambda sert à indiquer à Python que l'on souhaite créer une fonction anonyme (sans nom) qui prend un argument number et renvoie le carré de ce nombre.

# Il existe même une manière encore plus concise : les fonctions lambda auto-appelées (self-called).
# Elles permettent d'utiliser une fonction sans stocker le nom de cette fonction en mémoire.

(lambda x: x ** 2)(5) # renvoie également 25


# Exemple pour les listes :

# Nous connaissons déjà la syntaxe pour créer une liste en Python à partir d'une boucle.
# Par exemple, créons la table de multiplication de 3 :

resultats = []
for i in range(10):
    resultats.append(3 * i)

print(resultats) # affiche [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# Il est possible d'utiliser une syntaxe abrégée pour créer une liste à partir d'une boucle, appelée "list comprehension".

resultats_short = [3 * i for i in range(10)]
print(resultats_short) # affiche également [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# Nous pouvons même ajouter une condition pour filtrer les résultats. 
# Par exemple, créons la table de multiplication de 3, mais uniquement pour les nombres pairs :

resultats_pairs = [3 * i for i in range(10) if (3 * i) % 2 == 0]
print(resultats_pairs) # affiche [0, 6, 12, 18, 24]

# Dans ce cas, le if sert de filtre il est donc placé après la boucle for.

# Dans le cas où nous avons un if et un else, la syntaxe est légèrement différente.
# Par exemple, créons une liste qui contient "pair" si le nombre est pair et "impair" si le nombre est impair :

resultats_pair_impair = ["pair" if i % 2 == 0 else "impair" for i in range(10)]
print(resultats_pair_impair) # affiche ['pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair', 'pair', 'impair']

# Dans ce cas, le if et le else sont placés avant la boucle for.
# Ici, le if et le else servent à déterminer la valeur à ajouter à la liste en fonction de la condition.