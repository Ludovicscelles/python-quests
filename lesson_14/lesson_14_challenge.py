"""
Pour valider ce challenge, tu dois répondre aux questions ci-dessous en trouvant la Regex qui te permet d'obtenir le résultat attendu.
Texte à utiliser pour ce challenge :

"Matrix (31/03/1999) - 130 minutes. IMDB note 9/10 (https://www.imdb.com/title/tt0133093). 
Thomas A. Anderson (Keanu Reeves), un jeune informaticien connu dans le monde du hacking sous le pseudonyme de Neo, est contacté via son ordinateur par ce qu’il pense être un groupe de hackers. 
Ils lui font découvrir que le monde dans lequel il vit n’est qu’un monde virtuel, la matrice, dans lequel les êtres humains sont gardés sous contrôle. 
Morpheus (Laurence Fishburne), le capitaine du Nebuchadnezzar, contacte Neo et pense que celui-ci est l’Élu qui peut libérer les êtres humains du joug des machines et prendre le contrôle de la matrice"

Copie le texte ci-dessus affecte le à une variable appelée 'texte'. Tu as vu quelques fonctions du module re dans la quête, et pour répondre aux questions ci-dessous, tu utiliseras la fonctions findall()


"""

texte = "Matrix (31/03/1999) - 130 minutes. IMDB note 9/10 (https://www.imdb.com/title/tt0133093). " \
"Thomas A. Anderson (Keanu Reeves), un jeune informaticien connu dans le monde du hacking sous le pseudonyme de Neo, est contacté via son ordinateur par ce qu’il pense être un groupe de hackers. " \
"Ils lui font découvrir que le monde dans lequel il vit n’est qu’un monde virtuel, la matrice, dans lequel les êtres humains sont gardés sous contrôle. " \
"Morpheus (Laurence Fishburne), le capitaine du Nebuchadnezzar, contacte Neo et pense que celui-ci est l’Élu qui peut libérer les êtres humains du joug des machines et prendre le contrôle de la matrice"


# Exemple : je recherche toutes les suites de chiffres ('31', '03', '1999', '130', '9', '10', '0133093') contenues dans le texte

import re

text_numbers = re.findall(r'\d+', texte)
print(text_numbers) 


# 1 Trouve l'expression régulière qui cherche la seule occurrence du deuxième prénom de Néo (soit le A. de "Thomas A. Anderson).

second_name = re.findall(r'Thomas\s([A-Z]\.)\sAnderson', texte)
print(second_name) 

# other way to do it
second_name2 = re.findall(r'A\.', texte)
print(second_name2)


# 2. Trouve l'expression régulière qui cherche la date contenue dans le document.

date = re.search(r'\d{2}/\d{2}/\d{4}', texte)
print(date.group())  

# Other way to do it
date2 = re.search(r'\d+/\d+/\d+', texte)
print(date2.group())  


# 3. Trouve l'expression qui cherche la note contenue dans le texte, 
# sans pour autant sélectionner une partie de la date (tu peux t'aider du caractère espace avant la note)

note = re.search(r' \d{1}/\d{2}', texte)
print(note.group())  

# 4. Trouve l'expression régulière qui renvoie les mots ayant au moins 14 caractères 
# (tu devrais trouver l'age du capitaine, à moins que ça ne soit son vaisseau !)

words_14_char_or_more = re.findall(r'\b\w{14,}\b', texte)
print(words_14_char_or_more)


# Trouve l'expression régulière qui correspond à l'url de la fiche du film sur IMDB https://www.imdb.com/title/tt0133093 
# (attention à ne pas sélectionner les parenthèses)

url_pattern = r'https?://[^\s)]+'

url = re.search(url_pattern, texte)
if url:
  print(url.group())