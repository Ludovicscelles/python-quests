# - upper() : Convertit tous les caractères d'une chaîne en majuscules.

word = "bonjour"
print(word.upper())  # Affiche "BONJOUR"
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

# - split() : Divise une chaîne en une liste de sous-chaînes en utilisant un séparateur.
fairy_tale = "Il était une fois, dans un pays lointain"
fairy_tale_words = fairy_tale.split(", ")
print(fairy_tale_words)  # Affiche ['Il était une fois', 'dans un pays lointain']
print()

# - append() : Ajoute un élément à la fin d'une liste.
ma_liste = [1, 2, 3]
ma_liste.append(4)
print(ma_liste)  # Affiche [1, 2, 3, 4]
print()

# - remove() : Supprime la première occurrence d'un élément dans une liste.
ma_liste = [1, 2, 3]
if 2 in ma_liste:
    ma_liste.remove(2)
print(ma_liste)  # Affiche [1, 3]
print()

# - sort() : Trie les éléments d'une liste par ordre croissant.
# Cette méthode modifie la liste originale et renvoie None.
# Si vous voulez conserver l'originale, nous pouvons créer une copie avant de trier.
ma_liste = [5, 2, 8, 1, 3]
sorted_list = ma_liste.copy()  # Crée une copie de la liste pour ne pas modifier l'originale
sorted_list.sort()
print(sorted_list)  # Affiche [1, 2, 3, 5, 8]

# - keys() : Retourne une vue des clés du dictionnaire.
mon_dictionnaire = {"nom": "Alice", "âge": 30, "ville": "Paris"}
print(mon_dictionnaire.keys())  # Affiche dict_keys(['nom', 'âge', 'ville'])

# - values() : Retourne une vue des valeurs du dictionnaire.
print(mon_dictionnaire.values())  # Affiche dict_values(['Alice', 30, 'Paris'])

# - items() : Retourne une vue des paires clé-valeur du dictionnaire.
print(mon_dictionnaire.items())  # Affiche dict_items([('nom', 'Alice'), ('âge', 30), ('ville', 'Paris')])

# len() : Retourne le nombre d'éléments dans un objet (chaîne, liste, dictionnaire, etc.).
ma_chaine = "Bonjour"
print(len(ma_chaine))  # Affiche 7
ma_liste = [1, 2, 3, 4, 5]
print(len(ma_liste))  # Affiche 5
mon_dictionnaire = {"nom": "Alice", "âge": 30, "ville": "Paris"}
print(len(mon_dictionnaire))  # Affiche 3