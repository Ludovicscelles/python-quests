"""
Afin de faciliter la recherche d’un livre particulier, la bibliothèque municipale s’est dotée d’un système très perfectionné, à base de fiches en carton. 
Malheureusement, un bibliothécaire stagiaire s’est trompé dans la création des fiches et, à chaque fois, il a écrit le nom de l’auteur avant le titre du livre, au lieu de faire l’inverse !

Votre travail consiste à lire le contenu d’une fiche et à remettre les informations dans l’ordre.

Contraintes
Il y a toujours 6 titres de livres (et donc 6 noms d’auteurs) sur chaque fiche.

Les titres de livres et les noms d’auteurs font toujours moins de 200 caractères de long.

Entrée
Pour chacun des 6 livres, une ligne contenant le nom de l’auteur, et une ligne contenant le titre du livre.

Sortie
Pour chacun des livres, vous devez afficher sur une ligne le titre du livre, puis sur la ligne suivante le nom de l’auteur.

Exemple
entrée :

George ORWELL
1984
Pierre BOULLE
La planete des singes
Isaac ASIMOV
Les robots
Rene BARJAVEL
La nuit des temps
Arthur C. CLARKE
2001 : L'odyssee de l'espace
H.G. WELLS
La guerre des mondes
sortie :

1984
George ORWELL
La planete des singes
Pierre BOULLE
Les robots
Isaac ASIMOV
La nuit des temps
Rene BARJAVEL
2001 : L'odyssee de l'espace
Arthur C. CLARKE
La guerre des mondes
H.G. WELLS


"""

# books_number = 6
# books = []

# for book in range(books_number):
#   author = input()
#   title = input()
#   books.append(title)
#   books.append(author)
  
# for book in books:
#   print(book)


# Comparer deux chaînes de caractères
# Pour comparer deux chaînes de caractères, on peut utiliser les opérateurs de comparaison (<, >, <=, >=, ==, !=). 
# Ces opérateurs comparent les chaînes de caractères en fonction

# exemple :

# line1 = "Maitre Renard, par l'odeur alleche"
# line2 = "Lui tint a peu pres ce langage !"
# print("Selon l'ordre lexicographique, ", end="")
# if line1 < line2:
#     print(f"'{line1}' est avant '{line2}'")
# elif line1 > line2:
#     print(f"'{line1}' est après '{line2}'")
# else:
#     print(f"'{line1}' est egal a '{line2}'")


"""
Priorité alphabétique 

La plupart des livres de la bibliothèque dorment sagement sur les étagères, sans que personne ne les ouvre pendant de longs mois, voire des années. 
Mais il y a toujours quelques livres très demandés et, parfois, un même livre est demandé en même temps par deux personnes !

Afin d’éviter les soupçons de favoritisme, la règle suivante a été mise en place : si deux personnes demandent simultanément le même ouvrage, alors la personne qui l’aura est celle dont le nom est alphabétiquement le plus petit.

Vous devez écrire un programme permettant de résoudre automatiquement les éventuels litiges.

Contraintes
Chaque nom est composé uniquement de lettres majuscules, sans espaces.

Sa longueur sera au plus égale à 50.

Entrée
Sur la première ligne, le nom de la première personne.

Sur la seconde ligne, le nom de la seconde personne.

Sortie
Le nom le plus petit selon l’ordre alphabétique, c’est-à-dire le nom qui vient en premier selon cet ordre.

Si les deux noms sont égaux, il ne faut rien afficher car la personne a voulu tricher en faisant deux demandes d’un seul coup.

"""

# borrower_1 = input()
# borrower_2 = input()

# if borrower_1 < borrower_2:
#   print(borrower_1)
# elif borrower_1 > borrower_2:
#   print(borrower_2)
# else:
#   print()

# other way to do it

# borrower_1 = input()
# borrower_2 = input()

# if borrower_1 != borrower_2:
#   print(min(borrower_1, borrower_2))


""""
Une ligne sur deux 

En parcourant de vieux livres, vous tombez sur un certain nombre de textes, anodins au premier regard. À y regarder de plus près, ils prennent un tout autre sens, une fois qu’on ne lit qu’une ligne sur deux (la première, la troisième, la cinquième....).

Vous décidez d’écrire un programme permettant d’extraire uniquement les lignes impaires d’un texte donné.

Contraintes
Chaque ligne de texte contient au plus 100 caractères.

Entrée
Sur la première ligne un entier, nbLignes : le nombre total de lignes du texte.

Les nbLignes lignes suivantes contiennent alors le texte.

Sortie
Vous devez afficher uniquement les lignes impaires.

Exemple
entrée :

13
Mon assistant programmeur est toujours en train de
travailler a son bureau avec assiduite et diligence, sans jamais
perdre son temps en jasant avec ses collegues. Jamais il ne
refuse de passer du temps pour aider les autres et malgre cela, il
termine ses projets a temps. Tres souvent, il rallonge ses
heures pour terminer son travail, parfois meme en sautant les
pauses cafe. Il est une personne qui n'a absolument aucune
vanite en depit de ses accomplissements remarquables et de sa grande
competence en informatique. C'est le genre d'employe de qui on
parle avec grande estime et respect, le genre de personne dont on ne
peut se passer. Je crois fermement qu'il est pret pour la
promotion qu'il demande, considerant tout ce qu'il nous ap-
porte. L'entreprise en sortira grande gagnante.
sortie :

Mon assistant programmeur est toujours en train de
perdre son temps en jasant avec ses collegues. Jamais il ne
termine ses projets a temps. Tres souvent, il rallonge ses
pauses cafe. Il est une personne qui n'a absolument aucune
competence en informatique. C'est le genre d'employe de qui on
peut se passer. Je crois fermement qu'il est pret pour la
porte. L'entreprise en sortira grande gagnante.


"""

# lines_number = int(input())
# text_lines = []

# for id_line in range(lines_number):
#   line = input()
#   text_lines.append(line)

# for id_line in range(lines_number):
#   if id_line % 2 == 0:
#     print(text_lines[id_line])


""""
Résumés de livres

À la recherche de l'unique livre contenant les informations qui vous intéressent, vous souhaitez utiliser le grand index de la bibliothèque, celui dans lequel chaque livre est normalement référencé. En particulier, chaque titre de livre est accompagné d'un petit résumé de celui-ci, afin de pouvoir donner plus d'informations que le titre seul.

Or, le résumé de certains livres a parfois été fait très rapidement et ne contient pas suffisamment d'informations. Par exemple "Animaux" n'est pas un résumé correct !

Étant donnée la longueur minimale acceptable d'un résumé, vous décidez d'analyser l'index et de signaler automatiquement aux bibliothécaires les livres ayant des résumés trop courts, afin qu'ils puissent les compléter.

Contraintes
La longueur de chaque titre de livre et de chaque résumé n'excèdera jamais 1000 caractères.

Entrée
Sur la première ligne, un entier nbLivres, le nombre total de livres.

Sur la deuxième ligne, un entier longueurMinimale, la longueur minimale acceptable pour un résumé de livre.

Les 2 * nbLivres lignes suivantes contiennent, de manière alternée, un titre de livre et le résumé associé.

Sortie
Vous devez afficher, à raison d’un par ligne, le titre des livres dont le résumé n'est pas assez long, c'est-à-dire dont la longueur n'est pas au moins égale à longueurMinimale.

Exemple
entrée :

2
60
En attendant Godot
Deux clochards attendent Godot. Mais Godot ne vient pas.
Le Livre de la jungle
Moogli est eleve par les loups, Baloo l’ours, Bagheera la panthere. 
Shere Khan veut le manger, mais Moogli le tue. Il finit par vivre dans un village d'hommes.
sortie :

En attendant Godot


"""

# books_number = int(input())
# minimal_length = int(input())


# for book in range(books_number):
#   title = input()
#   report = input()
  
#   if len(report) < minimal_length:
#     print(title)


"""
Lire ou ne pas lire, telle est la question

Les employés de la bibliothèque, constamment entourés de livres, n’ont jamais le temps de lire tous les livres qu’ils souhaiteraient. 
Chacun a donc mis au point son propre algorithme de sélection, et l’un d’entre eux a choisi un système basé sur la longueur des titres des livres !

Sur une étagère sont alignés tous les livres qui l’intéressent. Chaque mois, cette personne commence par lire le premier livre présent sur l’étagère, puis le second et ainsi de suite jusqu’à la fin. 
Seulement, elle ne lira un livre que si son titre est strictement plus long que ceux de tous les livres qu’elle a lus pendant le mois. Si ce n’est pas le cas, elle enlève le livre de l’étagère, sans le lire.

Étant donnée une liste de titres de livres possibles pour le mois suivant, donnés dans l’ordre où ils apparaissent dans l’étagère, vous devez déterminer lesquels elle va lire.

Contraintes
Chaque titre de livre contiendra au plus 1000 caractères.

Entrée
Sur la première ligne, un entier nbLivres, le nombre total de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Sortie
La liste des titres respectant la règle donnée dans l’énoncé.

Exemple
entrée :

6
Les Facheux
Le Malade imaginaire
Les Femmes savantes
Les Fourberies de Scapin
L'Avare
Le Bourgeois gentilhomme
sortie :

Les Facheux
Le Malade imaginaire
Les Fourberies de Scapin

"""

# books_number = int(input())
# titles_list = []

# for book in range(books_number):
#   title = input()
#   titles_list.append(title)

# max_length_title = 0

# for title in titles_list:
#   if len(title) > max_length_title:
#     print(title)
#     max_length_title = len(title)

# Other way to do it without storing the titles in a list

# book_number = int(input())
# max_length_title = 0

# for book in range(book_number):
#   title = input()
#   if len(title) > max_length_title:
#     print(title)
#     max_length_title = len(title)



# Lire un mot individuellement

# Pour afficher certains mots d’une phrase, on peut utiliser la méthode split() qui permet de découper une chaîne de caractères en plusieurs sous-chaînes, en utilisant un séparateur.

# Exemple :

ligne = "Le renard brun rapide saute par-dessus le chien paresseux"
mots = ligne.split(" ")

print(ligne)

# Pour afficher les premiers et quatrièmes mots de la phrase, on peut utiliser l’indexation des listes :
print(mots[0])
print(mots[3])

# Autre façon de faire:

ligne = "Le renard brun rapide saute par-dessus le chien paresseux"
mots = ligne.split(" ")

elements = [0, 3]
print(ligne)
for element in elements:
  print(mots[element])

# Pour afficher plusieurs fois le même mot

# Si en entrée, on a :
# 5 TRUCS

# On peut faire :

# mots = input().split(" ")
# nombre = int(mots[0])
# mot = mots[1]

# for i in range(nombre):
#   print(mot)

# On a donc utilisé la méthode split() pour découper la chaîne de caractères en deux parties, puis on a converti la première partie en entier avec int().


"""
Fiches d’inscription

Au sein de la bibliothèque municipale, toutes les personnes souhaitant emprunter un livre doivent s'enregistrer en indiquant leurs noms et prénoms sur une fiche individuelle conservée à l'accueil.

L'habitude veut qu'ils écrivent d'abord leur nom puis leur prénom, ce qui permet de classer les fiches par ordre alphabétique et permet de rapidement retrouver la fiche qu'on cherche.

Malheureusement, depuis un mois, dans toutes les nouvelles fiches créées les personnes ont indiqué en premier leur prénom puis leur nom !

Votre travail consiste à lire ces couples de prénoms et noms et à les afficher dans le bon ordre.

Contraintes
Chaque nom et prénom est au plus de longueur 100 et ne contient pas d'espace.

Entrée
Sur la première ligne, un entier nbPersonnes : le nombre total de personnes concernées.

Sur chacune des nbPersonnes suivantes, un prénom et un nom, séparés par une espace.

Sortie
Pour chaque personne, vous devez écrire sur la même ligne son nom, puis son prénom, séparés par une espace.

Exemple
entrée :

4
Alan Turing
Ada Lovelace
Donald Knuth
Claude Shannon
sortie :

Turing Alan 
Lovelace Ada 
Knuth Donald
Shannon Claude


"""

# people_nb = int(input())

# for people in range(people_nb):
#   first_name, last_name = input().split(" ")
#   print(last_name, first_name)


# Lire plusieurs chiffres entiers:

# On peut lire des entiers sur la même ligne en utilisant la méthode split() pour découper la chaîne de caractères, puis en convertissant chaque sous-chaîne en entier avec int().

# Exemple :

# mots = input().split(" ")
# longeur = int(mots[0])
# largeur = int(mots[1])
# area = longeur * largeur
# print(area)

# On peut aussi utiliser la fonction map() pour appliquer la fonction int() à chaque élément de la liste obtenue avec split().

# longeur, largeur = map(int, input().split(" "))
# area = longeur * largeur
# print(area)

"""
Analyse de fréquence

En étudiant différents types de textes (romans, lois, article de journaux…), on se rend compte que non seulement les mots utilisés ne sont pas les mêmes mais aussi que leurs longueurs sont statistiquement différentes : par exemple, il est beaucoup plus fréquent de trouver de longs mots complexes dans un article de loi que dans un livre pour enfants.

Afin d’essayer de déterminer automatiquement à quelle catégorie appartient un livre, on souhaite déterminer le nombre de mots de 1 lettre, 2 lettres, 3 lettres… qu’il contient.

Contraintes
Le texte contient un ensemble de mots, séparés par des espaces, sans aucun signe de ponctuation.

Chaque mot contient au plus 100 caractères.

Entrée
La première ligne contient deux entiers : nbLignes et nbMots.

Chacune des nbLignes lignes suivantes contient nbMots mots.

Sortie
Pour chaque longueur de mot possible, et uniquement s’il y avait des mots de cette longueur dans le texte, vous devez afficher sur une ligne la longueur et le nombre de mots de cette longueur, séparés par un deux-points (il faut mettre un espace de chaque côté du deux-points).

Exemple
entrée :

2 7
Qui vole un oeuf vole un boeuf
Une abeille vaut mieux que mille mouches
sortie :

2 : 2
3 : 3
4 : 4
5 : 3
7 : 2


"""


# lines_number, words_number = map(int, input().split(" "))

# words_length = {}

# for line in range(lines_number):

#   words = input().split(" ")

#   for word in words:

#     len_w = len(word)

#     if len_w in words_length:

#       words_length[len_w] += 1
    
#     else:

#       words_length[len_w] = 1

# print(words_length)

# for length in sorted(words_length):
#   print(f"{length} : {words_length[length]}")


# Other way to do it:

# lines_number, words_number = map(int, input().split(" "))

# max_word_length = 100

# words_length = [0] * (max_word_length + 1)

# for line in range(lines_number):

#   words = input().split(" ")

#   for word in words:

#     len_w = len(word)

#     words_length[len_w] += 1


# for length, count in enumerate(words_length):
#   if count > 0:
#     print(f"{length} : {count}")


# print(words_length)



"""
Impression d’étiquettes

Les sous-sols de la bibliothèque municipale sont remplis de milliers de cartons d’archives. 
Afin d’éviter de passer leurs journées avec la tête tournée à 90 degrés pour pouvoir lire ce qui est écrit sur ces cartons, les bibliothécaires ont adopté un système d’étiquettes où les mots sont écrits de haut en bas avec une seule lettre par ligne.

Étant donné un texte écrit normalement, sur une seule ligne, vous devez afficher l’étiquette correspondante, avec un seul caractère par ligne.



"""

# title = input().split(" ")

# for word in title:
#   for letter in word:
#     print(letter)
#   print()

# Other way to do it:

# title = input()

# for letter in title:
#   print(letter)

"""
Écriture en miroir


Alors que vous parcourez de très vieux livres, à la recherche d’indications sur le livre qui vous intéresse en particulier, vous tombez sur un langage que vous ne connaissez pas !

À y regarder de plus près, il s’agit des mêmes mots que ceux que vous utilisez tous les jours, mais tout le texte est écrit "en miroir" : toutes les lettres sont écrites de droite à gauche.

Bien que vous arriviez à déchiffrer les textes présents dans ces livres, cela vous prend beaucoup de temps et vous fatigue beaucoup. 

Vous décidez d’écrire un programme pour remettre automatiquement dans l’ordre les textes.

Contraintes
Chaque ligne de texte contient moins de 1000 caractères.

Entrée
Sur la première ligne, un entier nbLignes, le nombre de lignes du texte.

Les nbLignes suivantes contiennent chacune une ligne de texte qu’il faut inverser.

Sortie
Pour chaque ligne du texte original, vous devez l’afficher de manière inversée.

Exemple
entrée :

2
tniop a ritrap tuaf li riruoc ed tres en neiR
egangiomet nu tnos ne eutroT al te erveiL eL
sortie :

Rien ne sert de courir il faut partir a point
Le Lievre et la Tortue en sont un temoignage


"""

# lines_number = int(input())

# for line_id in range(lines_number):
#   string = input()

#   reversed_string = ""
#   index = len(string)

#   while index:
#     index -= 1
#     reversed_string += string[index]

#   print(reversed_string)

# Other way to do it:

# lines_number = int(input())

# for line_id in range(lines_number):
#   string = input()
#   length = len(string)
#   for character_id in range(length):
#     print(string[length - 1 - character_id], end = "")
#   print()

  # Comparer deux caractères

# Pour comparer deux caractères, on peut utiliser les opérateurs de comparaison (<, >, <=, >=, ==, !=). 
# Ces opérateurs comparent les caractères en fonction de leur code ASCII.

# Exemple :

name = "Ludovic"

if name[0] < name[4]:
    print(f"Le caractere '{name[0]}' est avant le caractere '{name[4]}' dans l'ordre ASCII")
elif name[0] > name[5]:
    print(f"Le caractere '{name[0]}' est apres le caractere '{name[4]}' dans l'ordre ASCII")
else:
    print(f"Le caractere '{name[0]}' est egal au caractere '{name[4]}' dans l'ordre ASCII")

# Il est aussi possible un caractère d'une chaîne à un caractère directement dans le code, par exemple :

family_name = "Di Feliciantonio"

if family_name[0] == "D":
    print(f"Le nom de famille commence par la lettre D")
if family_name[3] <= "M":
    print(f"La quatrième lettre du nom de famille est avant ou égale à la lettre M de l'alphabet")
if family_name[2] == " ":
    print(f"La troisième lettre du nom de famille est un espace")

"""
Inscription d’étudiants

Comme chaque année, lors de la rentrée universitaire, de nombreux étudiants viennent s’inscrire à la bibliothèque et une longue file d’attente se forme. 
Afin d’essayer d'accélérer les choses, les fiches d’inscription de tous les étudiants ont déjà été préparées et ils n’ont plus qu’à les récupérer.

Trois personnes sont en charge de distribuer les fiches : la première s’occupe des étudiants dont le nom commence par une lettre comprise entre A et F (inclus), 
la seconde personne des étudiants dont le nom commence par une lettre comprise entre G et P (inclus) et la troisième du reste des étudiants.

Quand un nouvel étudiant arrive, il donne son nom et il faut lui indiquer quelle personne il doit aller voir.

Contraintes
Les noms des étudiants font moins de 50 caractères de long et commencent par une lettre majuscule.

Entrée
Un nom d’étudiant.

Sortie
Un entier, 1, 2 ou 3, selon que l’étudiant doit aller voir la première, la seconde ou la troisième personne.

Exemples
Exemple 1
entrée :

Donald
sortie :

1
Exemple 2
entrée :

Picsou
sortie :

2

"""

# name = input()
# first_letter = name[0]

# if first_letter <= "F":
#     print(1)
# elif first_letter <= "P":
#     print(2)
# else:
#     print(3)

"""
ngms sns vlls

Les personnes travaillant à la bibliothèque aiment particulièrement se poser des petites énigmes, d’inspiration littéraires. 
Cette fois-ci, Agrarelle a décidé de créer des énigmes basées sur des titres de livres : elle va supprimer l’ensemble des voyelles (et les espaces) d’un titre et du nom de son auteur et ses collègues devront retrouver le titre original (ainsi que le nom de l’auteur).

Contraintes
Le titre et le nom de l’auteur font chacun moins de 100 caractères.

Ils ne contiennent que des lettres majuscules et des espaces.

Entrée
Sur la première ligne, le titre du livre.

Sur la seconde ligne, le nom de l’auteur.

Sortie
Sur la première ligne, le titre du livre, sans aucune voyelle, ni espace.

Sur la seconde ligne, le nom de l’auteur, sans aucune voyelle, ni espace.

Exemple
entrée :

AUTANT EN EMPORTE LE VENT
MARGARET MITCHELL
sortie :

TNTNMPRTLVNT
MRGRTMTCHLL


"""

# title = input()
# author = input()

# vowels = "AEIOUY"

# for character in title:
#     if character not in vowels and character != " ":
#       print(character, end= "")

# print()

# for character in author:
#     if character not in vowels and character != " ":
#       print(character, end= "")


# title = input()
# author = input()

# vowels_and_space = "AEIOUY "

# title_to_guess = "".join(c for c in title if c not in vowels_and_space)
# author_to_guess = "".join(c for c in author if c not in vowels_and_space)

# print(title_to_guess)
# print(author_to_guess)


"""
La bataille

Vous avez sûrement déjà joué, étant enfant, au jeu de cartes appelé la « bataille ». 
Les enfants algoréens aiment aussi beaucoup jouer à une variante bien plus simple de ce jeu, et vous devez faire l’arbitre des parties. 
Comme il y a beaucoup d’enfants souhaitant jouer en même temps et que vous ne pouvez pas tout surveiller, vous décidez d’écrire un programme informatique pour déterminer le vainqueur de chaque partie.

Une partie se déroule ainsi :

On part d’un jeu contenant 52 cartes, chaque carte étant une lettre entre A et M, et chaque lettre étant présente 4 fois (avec différentes couleurs, mais on ne s’en occupera pas ici).
Les cartes, face cachée, sont mélangées et séparées en deux paquets (pas forcément de même taille !).
Les deux joueurs retournent la première carte de leur paquet : si les deux cartes sont identiques ils continuent à jouer, sinon celui qui a la carte la plus forte, c’est-à-dire la plus petite selon l’ordre alphabétique, gagne la partie.
Si un joueur n’a plus de carte, il perd ! Et oui, ce n’est pas très juste !
Si les deux joueurs n’ont en même temps plus de cartes, alors il y a égalité complète.
Étant donnés les deux paquets de cartes, à vous de déterminer le gagnant.

Entrée
L'entrée contient deux lignes, correspondant respectivement aux cartes du joueur 1 et du joueur 2, dans l'ordre. Un jeu de cartes est constitué uniquement de lettre majuscules entre A et M (sans espaces).

Sortie
Sur la première ligne, il faut indiquer « 1 », « 2 » ou « = » selon que le gagnant est le premier ou le second joueur, ou bien qu’il y a égalité complète.

Sur la seconde ligne, il faut indiquer le nombre d’égalités qui ont eu lieu avant que le jeu ne se termine.

Exemples
Exemple 1
entrée :

AABBDCCDEEFFGGHHIIJJKKLLMM
AABBCCDDEEFFGGHHIIJJKKLLMM
sortie :

2
4
Exemple 2
entrée :

AA
AABBCCDDEEFFGGHHIIJJKKLLMMBBDCCDEEFFGGHHIIJJKKLLMM
sortie :

2
2
Commentaires
L'exemple 1 se déroule comme suit :

A contre A, égalité ;
A contre A, égalité ;
B contre B, égalité ;
B contre B, égalité ;
D contre C : le C l'emporte.
C'est donc le joueur 2 qui remporte la partie, après 4 égalités.

Dans l'exemple 2, après deux égalités, le joueur 1 n'a plus de carte et donc perd la partie.



"""

# player_1_cards = input()
# player_2_cards = input()

# len_game_1 = len(player_1_cards)
# len_game_2 = len(player_2_cards)

# equality_count = 0

# for i in range(min(len_game_1, len_game_2)):

#     card_p1 = player_1_cards[i]
#     card_p2 = player_2_cards[i]

#     if card_p1 < card_p2:
#         print(1)
#         break
#     elif card_p1 > card_p2:
#         print(2)
#         break
#     else:
#         equality_count += 1
#         continue
        
# else:
#     if len_game_1 < len_game_2:
#         print(2)
#     elif len_game_1 > len_game_2:
#         print(1)
#     else:
#         print("=")


# print(equality_count) 

# other way to do it: 

# player_1_cards = input()
# player_2_cards = input()
# round = 0

# len_game_1 = len(player_1_cards)
# len_game_2 = len(player_2_cards)

# while round < len_game_1 and round < len_game_2 and player_1_cards[round] == player_2_cards[round]:
#     round = round + 1
# if round == len_game_1 and round == len_game_2:
#     print("=")
# elif round == len_game_2 or (round < len_game_1 and player_1_cards[round] < player_2_cards[round]):
#     print(1)
# else:
#     print(2)
# print(round)

# Other way to do it:

# player_1_cards = input()
# player_2_cards = input()

# len_game_1 = len(player_1_cards)
# len_game_2 = len(player_2_cards)

# equal_round = 0

# for card_p1, card_p2 in zip(player_1_cards, player_2_cards):

#     if card_p1 < card_p2:
#         print(1)
#         break
#     elif card_p1 > card_p2:
#         print(2)
#         break
#     else:
#         equal_round += 1

# else:

#     if len_game_1 < len_game_2:
#         print(2)
#     elif len_game_1 > len_game_2:
#         print(1)
#     else:
#         print("=")

# print(equal_round)

"""
Analyse d’une langue

Au cours des siècles une langue évolue, et non seulement les mots apparaissent ou disparaissent, mais certaines lettres deviennent plus utilisées ou au contraire moins utilisées.

Afin de pouvoir rapidement analyser de nombreux textes, on souhaite mettre au point un programme calculant combien de fois une lettre donnée est présente au sein d’un texte.

Contraintes
Chaque ligne de texte contient au plus 1000 caractères.

Entrée
Sur la première ligne, la lettre majuscule dont on doit chercher le nombre d’apparition dans le texte.

Sur la seconde ligne, un entier nbLignes le nombre de lignes du texte.

Sur les nbLignes lignes suivantes, le texte, ne contenant aucune lettre minuscule.

Sortie
Un seul entier, le nombre d’apparitions de la lettre au sein du texte.

Exemple
entrée :

E
2
JE VOUS REMECTZ A LA GRANDE CHRONICQUE PANTAGRUELINE 
RECONGNOISTRE LA GENEALOGIE ET ANTIQUITE DONT NOUS EST VENU GARGANTUA
sortie :

16

"""

letter = input()
number_of_lines = int(input())

letter_count = 0

for _ in range(number_of_lines):
    line = input()
    for character in line:
        if character == letter:
            letter_count += 1

print(letter_count)

# Other way to do it:



letter = input()
number_of_lines = int(input())

letter_count = sum(character == letter for _ in range(number_of_lines) for character in input())