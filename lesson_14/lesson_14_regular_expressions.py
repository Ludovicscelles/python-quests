# Les Expressions Régulières

# Les expressions régulières sont un outil puissant pour la manipulation de chaînes de caractères. 
# Elles permettent de rechercher, remplacer et valider des motifs spécifiques dans des textes.
# Les expressions régulières sont souvent utilisées pour la validation de formats, l'extraction d'informations et le nettoyage de données.
# Elles sont largement utilisées dans de nombreux langages de programmation et outils de traitement de texte.

# Voici quelques concepts de base des expressions régulières :

# Recherche de motifs : Les expressions régulières permettent de définir des motifs spécifiques à rechercher dans une chaîne de caractères. 
# Par exemple, nous allons rechercher des vins millésimés 2016.

vin = [
    "Château Margaux 2016",
    "Domaine de la Romanée-Conti 2016",
    "Château Lafite Rothschild 2015",
    "Château Latour 2016",
    "Château Mouton 4561Rothschild 2014",
    "Château Haut-Brion 2016",
    "Château Cheval Blanc 2015",
    "Château Pétrus 2016",
    "Château d'Yquem 2016",
    "Château Palmer 2015"
]

import re

wine_names = [v for v in vin if re.search(r'\b2016\b', v)]
print("Liste des vins millésimés 2016 :", wine_names)

# Rechercher le millésime dans une variable de chaîne de caractères

wine = "Château Margaux 2016 Délicieux et élégant"

import re

millesime = re.search(r'\b\d{4}\b', wine)
if millesime:
    print("Millésime trouvé :", millesime.group())

# re.search() renvoie le premier match trouvé dans la chaîne de caractères.

# Other way to do it 

wine_2 = "Bergerac 2016 Un vin rouge fruité et équilibré"

import re

millesime_2 = re.findall(r'\b\d{4}\b', wine_2)
if millesime_2:
    print(millesime_2)

# re.findall() renvoie tous les matchs trouvés dans la chaîne de caractères sous forme de liste.

# Autre utilisations du module re :

# re.split() : Cette fonction permet de diviser une chaîne de caractères en utilisant un motif spécifique comme séparateur.
# Par exemple, nous allons diviser une chaîne de caractères contenant des informations sur un vin en utilisant l'espace comme séparateur.

wine_info = "Château Margaux 2016 Délicieux et élégant"

import re

wine_info_split = re.split(r'\s+', wine_info)
print("Informations sur le vin divisées :", wine_info_split)

# re.sub() : Cette fonction permet de remplacer un motif spécifique dans une chaîne de caractères par une autre valeur.
# Par exemple, nous allons remplacer le millésime 2016 par 2020 dans une chaîne de caractères.

wine_info_2 = "Château Margaux 2016 Délicieux et élégant"

import re

wine_info_replaced = re.sub(r'\b2016\b', '2020', wine_info_2)
print("Informations sur le vin après remplacement :", wine_info_replaced)

# Différentes regex patterns :

# Recherche utilisant des métacaractères : 
# Les métacaractères sont des caractères spéciaux qui ont une signification particulière dans les expressions régulières.

# Dans les exemples suivants, nous allons explorer différents motifs d'expressions régulières pour rechercher des informations spécifiques dans des chaînes de caractères.

text = "The Saturn V was launched 13 times from Kennedy Space Center with no loss of crew or payload. As of 2021, the Saturn V remains the tallest, heaviest, and most powerful (highest total impulse) rocket ever brought to operational status, " \
"and it holds records for the heaviest payload launched and largest payload capacity to low Earth orbit (LEO) of 310,000 lb (140,000 kg), which included the third stage and unburned propellant needed to send the Apollo command and service " \
"module and Lunar Module to the Moon."

print("Texte à analyser :", text)

# Rechercher n'importe quel caractère : 

text_1 = re.findall(r'.', text)
print("Tous les caractères dans le texte :", text_1)

# Rechercher la présence d'un caractère facultatif :

text_2 = re.findall(r're?', text)
print("Présence du caractère 'r' suivi éventuellement de 'e' :", text_2)

# Rechercher si un motif est en début de texte :

text_3 = re.findall(r'^The', text)
print("Motif 'The' en début de texte :", text_3)

# Rechercher si un motif est en fin de texte :

text_4 = re.findall(r'Moon\.$', text)
print("Motif 'Moon.' en fin de texte :", text_4)

# Rechercher au moins un des deux motifs est présent :

text_5 = re.findall(r'Saturn|Apollo', text)
print("Présence de 'Saturn' ou 'Apollo' :", text_5)

# Rechercher une suite de caractères ou pour échapper des caractères spéciaux :

text_6 = re.findall(r'\d+', text)
print("Tous les chiffres dans le texte :", text_6)

# Rechercher si un motif est présent une ou plusieurs fois :

text_7 = re.findall(r'en+', text)
print("Présence de la lettre 'e' suivie d'une ou plusieurs lettres 'n' :", text_7)

# Définir le nombre exact d'occurrences du motif à rechercher :

text_8 = re.findall(r'\b\w{5}\b', text)
print("Mots de 5 lettres dans le texte :", text_8)

text_9 = re.findall(r'en{2}', text)
print("Présence de la lettre 'e' suivie exactement de deux lettres 'n' :", text_9)

# Pour rechercher un motif contenant des sous groupes de motifs :

text_10 = re.findall(r'(Saturn|Apollo) (V|command)', text)
print("Sous-groupes de motifs 'Saturn' ou 'Apollo' suivis de 'V' ou 'command' :", text_10)

text_11 = re.findall(r'([a-z]+) (\d+)', text)
print("Sous-groupes de motifs : lettres minuscules suivies de chiffres :", text_11)


# Recherche à l'aide de séquences d'échappement :

# Rechercher si un motif se trouve au début du texte :

text_12 = re.findall(r'\AThe', text)
print("Motif 'The' au début du texte :", text_12)

# Rechercher si un motif se trouve dans le texte mais pas au début d'un mot :

text_13 = re.findall(r'\Best', text)
print("Motif 'est' dans le texte mais pas au début d'un mot :", text_13)

# Rechercher si un motif se trouve dans le texte mais pas à la fin d'un mot :

text_14 = re.findall(r'est\B', text)
print("Motif 'est' dans le texte mais pas à la fin d'un mot :", text_14)

# Rechercher tous les éléments du texte qui ne contiennent aucun chiffre :

text_15 = re.findall(r'\D+', text)
print("Éléments du texte sans chiffres :", text_15)


# Rechercher tous les éléments du texte autre que les espacements :

text_16 = re.findall(r'\S+', text)
print("Éléments du texte autre que les espacements :", text_16)

# Rechercher tous les éléments du texte à l'exception des caractères alphanumériques :

text_17 = re.findall(r'\W+', text)
print("Éléments du texte à l'exception des caractères alphanumériques :", text_17)

# Rechercher si un motif se trouve à la fin du texte :

text_18 = re.findall(r'Moon.\Z', text)  
print("Motif 'Moon' à la fin du texte :", text_18)

# Rechercher si un motif se trouve dans le texte et au début d'un mot :

text_19 = re.findall(r'\blo', text)
print("Motif 'lo' au début d'un mot dans le texte :", text_19)

# Rechercher si un motif se trouve dans le texte et à la fin d'un mot :

text_20 = re.findall(r'lo\b', text)
print("Motif 'lo' à la fin d'un mot dans le texte :", text_20)

# Rechercher tous les éléments du texte qui contiennent des chiffres :

text_21 = re.findall(r'\d+', text)
print("Éléments du texte contenant des chiffres :", text_21)

# Rechercher tous les caractères alphanumériques dans le texte :

text_22 = re.findall(r'\w+', text)
print("Caractères alphanumériques dans le texte :", text_22)


# Recherche par ensemble de caractères :

# On se sert des crochets [] pour définir un ensemble de caractères à rechercher dans le texte.

# Recherche d'une liste de motifs spécifiques :

text_23 = re.findall(r'[aeiou]', text)
print("Présence des voyelles dans le texte :", text_23)

# Recherche d'une plage de caractères :

text_24 = re.findall(r'[a-m]', text)
print("Présence des lettres de 'a' à 'm' dans le texte :", text_24)

# Recherche d'une plage de chiffres :  

text_25 = re.findall(r'[0-9]', text)
print("Présence des chiffres de 0 à 9 dans le texte :", text_25)

text_26 = re.findall(r'[123]', text)
print("Présence des chiffres 1, 2 ou 3 dans le texte :", text_26)

# Recherche en excluant certains caractères :

text_27 = re.findall(r'[^aeiou]', text)
print("Présence de tous les caractères sauf les voyelles dans le texte :", text_27)

# Recherche d'un ou plusieurs motifs spécifiques :

text_28 = re.findall(r're[mvc]?', text)
print("Présence de 're' suivi éventuellement de 'm', 'v' ou 'c' dans le texte :", text_28)




