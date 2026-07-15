# Méthodes, Fonctions et Modules en Python

# En Python, une méthode est une fonction associée à un objet.
# Une fonction est un bloc de code réutilisable qui réalise une tâche précise.
# Un module est un fichier regroupant des fonctions, des classes et d'autres outils.

# Voici quelques exemples de méthodes couramment utilisées en Python :

# 1. Méthodes de chaîne de caractères (str)
# - upper() : Convertit tous les caractères d'une chaîne en majuscules.

word = "bonjour"
print(word.upper())  # Affiche "BONJOUR"
print()

# - lower() : Convertit tous les caractères d'une chaîne en minuscules.
phrase = "BONJOUR, COMMENT ÇA VA ?"
print(phrase.lower())  # Affiche "bonjour, comment ça va ?"
print()

# - strip() : 

# Sans argument, strip() supprime les espaces au début et à la fin d'une chaîne.
# Avec un argument, strip() supprime tous les caractères spécifiés aux deux extrémités de la chaîne.

texte = "   Python est génial !   "
print(texte.strip())  # Affiche "Python est génial !"
print()

texte2 = "RRRRRRRRRRRRRBonjour, comment ça va ?RRR"
print(texte2.strip("R"))  # Affiche "Bonjour, comment ça va ?"
# strip("R") supprime tous les caractères R présents aux deux extrémités, mais pas ceux situés au milieu.

# - replace() : Remplace une sous-chaîne par une autre dans une chaîne.
message = "J'aime la glace au chocolat"
nouveau_message = message.replace("au chocolat", "à la vanille")
print(nouveau_message)  # Affiche "J'aime la glace à la vanille"
print()

# - split() : Divise une chaîne en une liste de sous-chaînes en utilisant un séparateur.
fairy_tale = "Il était une fois, dans un pays lointain"
fairy_tale_words = fairy_tale.split(", ")
print(fairy_tale_words)  # Affiche ['Il était une fois', 'dans un pays lointain']
print()

# - join() : Concatène une liste de chaînes en une seule chaîne en utilisant un séparateur.
mots = ["Python", "est", "super"]
phrase = " ".join(mots)
print(phrase)  # Affiche "Python est super"
print()

# 2. Méthodes de liste (list)

# - append() : Ajoute un élément à la fin d'une liste.
ma_liste = [1, 2, 3]
ma_liste.append(4)
print(ma_liste)  # Affiche [1, 2, 3, 4]
print()

# - remove() : Supprime la première occurrence d'un élément dans une liste.
if 2 in ma_liste:
    ma_liste.remove(2)
print(ma_liste)  # Affiche [1, 3, 4]
print()

# - sort() : Trie les éléments d'une liste par ordre croissant.
# Cette méthode modifie la liste originale et renvoie None.
# Si vous voulez conserver l'originale, nous pouvons créer une copie avant de trier.
sorted_list = ma_liste.copy()  # Crée une copie de la liste pour ne pas modifier l'originale
sorted_list.sort()
print(sorted_list)  # Affiche [1, 3, 4]

# - reverse() : Inverse l'ordre des éléments d'une liste.
# De même, cette méthode modifie la liste originale et renvoie None.
# Pour conserver l'originale, nous pouvons créer une copie avant d'inverser.
reverse_list = ma_liste.copy()  # Crée une copie de la liste pour ne pas modifier l'originale
reverse_list.reverse()
print(reverse_list)  # Affiche [4, 3, 1]

# - index() : Retourne l'index de la première occurrence d'un élément dans une liste.
if 3 in ma_liste:
    index_de_3 = ma_liste.index(3)
print(index_de_3)  # Affiche 1
print()

# - count() : Compte le nombre d'occurrences d'un élément dans une liste.
numbers = [1, 2, 3, 2, 4, 2]
count_of_2 = numbers.count(2)
print(count_of_2)  # Affiche 3
print()

# 3. Méthodes de dictionnaire (dict)

# - keys() : Retourne une vue des clés du dictionnaire.
mon_dictionnaire = {"nom": "Alice", "âge": 30, "ville": "Paris"}
print(mon_dictionnaire.keys())  # Affiche dict_keys(['nom', 'âge', 'ville'])
print()

# - values() : Retourne une vue des valeurs du dictionnaire.
print(mon_dictionnaire.values())  # Affiche dict_values(['Alice', 30, 'Paris'])
print()

# - items() : Retourne une vue des paires clé-valeur du dictionnaire.
print(mon_dictionnaire.items())  # Affiche dict_items([('nom', 'Alice'), ('âge', 30), ('ville', 'Paris')])
print()

# keys(), values() et items() retournent des vues dynamiques, ce qui signifie que si le dictionnaire est modifié, les vues refléteront ces changements.

# 4. Fonctions intégrées utiles (built-in functions)

# eval() : Évalue une expression Python contenue dans une chaîne de caractères et retourne le résultat.
expression = "2 + 3 * 4"
resultat = eval(expression)
print(resultat)  # Affiche 14
print()

# Attention : eval() peut exécuter du code arbitraire, donc il doit être utilisé avec précaution.
# Il ne faut jamais utiliser eval() sur des entrées provenant d'un utilisateur ou d'une source non fiable, car cela peut entraîner des failles de sécurité.

# range() : Génère une séquence de nombres. Il est souvent utilisé dans les boucles for.
# Il genère un objet itérable de type range.
for i in range(5):
    print(i)  # Affiche les nombres de 0 à 4
print()

# Unicode

caractere = 'A'
point_de_code = ord(caractere)  # Obtient le point Unicode caractère
print(f"Le point de code Unicode de '{caractere}' est {point_de_code}")  # Obtient le code Unicode du caractère 'A' et l'affiche
print()
code_unicode = chr(65)  # Obtient le caractère correspondant au code Unicode
print(f"Le caractère correspondant au code Unicode 65 est '{code_unicode}'")  # Affiche "Le caractère correspondant au code Unicode 65 est 'A'"
print()

# 5. Fonctions anonymes (lambda functions)

# lambda : Permet de créer des fonctions anonymes (lambda functions).
# Exemple : une fonction lambda qui calcule le carré d'un nombre.
carre = lambda x: x ** 2
print(carre(5))  # Affiche 25

f = lambda x, y: x + y
print(f(3, 4))  # Affiche 7


# 6. Modules de la bibliothèque standard (standard library)

# getpass() 
# getpass.getpass() : Permet de saisir un mot de passe sans l'afficher à l'écran.
import getpass
mot_de_passe = getpass.getpass("Entrez votre mot de passe : ")  
print("Mot de passe saisi (non affiché pour des raisons de sécurité).")
print()

# os : 
# Le module os permet d'interagir avec le système d'exploitation.
# Il fonctionne notamment sur Windows, macOS et Linux.
# Certaines commande exécutées avec os.system() sont propre à un système
import os
import sys

if os.name == "nt":
    os.system("mode con: cols=100 lines=30")  # Commande Windows

elif sys.platform == "darwin":
    os.system("printf '\\033[8;30;100t'")  # Peut fonctionner dans certains terminaux macOS


# thread 
# Un thread est une unité d’exécution au sein d’un même processus. 
# Le module threading permet de lancer plusieurs tâches de manière concurrente.
# Le module threading fournit des classes et des fonctions pour créer et gérer des threads en Python.
from threading import Thread
from time import sleep

def afficher_message(nom):
    sleep(1)  # Simule un traitement long
    print(f"Bonjour, {nom} !")

# Création de deux threads pour exécuter la fonction afficher_message avec des arguments différents.
thread1 = Thread(target=afficher_message, args=("Alice",))
thread2 = Thread(target=afficher_message, args=("Bob",))

# Démarrage des threads
thread1.start()
thread2.start()

thread1.join()  # Attend que le thread1 se termine
thread2.join()  # Attend que le thread2 se termine



# 7. Modules externes (external modules)

# progressbar : Permet d'afficher une barre de progression dans la console.
# Pour utiliser progressbar, vous devez installer le module progressbar2 via pip.
# Exemple d'utilisation de progressbar pour afficher une barre de progression lors d'une boucle.
from progressbar import ProgressBar
from time import sleep

bar = ProgressBar(max_value=10)
for i in range(10):
    bar.update(i + 1)
    sleep(0.5)  # Simule un traitement long

# prettytable : Permet d'afficher des tableaux de manière lisible dans la console.
# Pour utiliser prettytable, vous devez installer le module prettytable via pip.
from prettytable import PrettyTable

# Création d'un tableau avec PrettyTable
table = PrettyTable()
table.field_names = ["Nom", "Âge", "Ville"]
# Ajout de lignes au tableau
table.add_row(["Alice", 30, "Paris"])
table.add_row(["Bob", 25, "Londres"])
# Affichage du tableau
print(table)

ice_cream = PrettyTable()
ice_cream.field_names = ["Saveur", "Coulis", "Supplément", "Prix"]
ice_cream.add_row(["Vanille", "Chocolat", "Chantilly", "3,50€"])
ice_cream.add_row(["Fraise", "Caramel", "Amandes", "4,00€"])
ice_cream.add_row(["Chocolat", "Framboise", "Noisettes", "4,50€"])
ice_cream.add_row(["Menthe", "Chocolat", "Biscuits", "4,00€"])
ice_cream.add_row(["Coco", "Mangue", "Noix de coco râpée", "4,50€"])
print(ice_cream) 