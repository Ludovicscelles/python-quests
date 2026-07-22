# Exception handling

# Les "exceptions" sont des erreurs qui se produisent pendant l'exécution d'un programme. 
# Python fournit un mécanisme pour gérer ces exceptions afin que le programme puisse continuer à s'exécuter même lorsqu'une erreur se produit.

# Nous allons apprendre à gérer les gérer les cas d'erreurs courants en Python.

# Connaissances théoriques.

# Lire les codes erreurs

# Afin de mieux comprendre les erreurs qui se produisent dans votre code, 
# il est important de lire attentivement les messages d'erreur générés par Python. 
# Ces messages fournissent des informations précieuses sur la nature de l'erreur et l'endroit où elle s'est produite.

# Demandons à Python un premier calcul : 12 divisé par 0. Cela va générer une erreur de type ZeroDivisionError.

"""x = 0
print("hello")
print(12 / x)"""  # Cela va générer une erreur de type ZeroDivisionError

# Nous obtenons ceci dans la console :
# Traceback (most recent call last):
#   File "lesson_19_exception_handling.py", line 20, in <module>
#     print(12 / x)  # Cela va générer une erreur de type ZeroDivisionError
# ZeroDivisionError: division by zero

# Python donne les indications suivantes sur l'erreur :

# - la position de l'erreur dans le code (ligne 20)
# - le code de l'erreur (ZeroDivisionError), accompagneé d'une explication sur l'erreur (division by zero).

# Exceptions handling

# Il s'agit maintenant de gérer ces erreurs via des exceptions.

# Pour le code précédent, on pourra le faire à la main, en vérifiant que x est différent de 0 avant de faire la division :

x = 0
print("hello")
if x != 0:
    print(12 / x)
else:
    pass
print()

# Mais il existe une autre manière plus propre de gérer les erreurs, en utilisant les blocs try et except.
# Ici, nous indiquons à Python "Essaye d'exécuter ce code, et si une erreur se produit, va dans l'exception":

x = 0
print("hello")

try:
   print(12 / x)
except :
    print("warning, you are trying to divide by 0")
print()

# Seulement, Python va attraper toutes les erreurs, et pas seulement celles de type ZeroDivisionError.
# Cela peut masquer d'autres types d'erreurs, et rendre le débogage plus difficile. 
# Il est donc préférable de spécifier le type d'erreur que l'on souhaite gérer.

x = 0
print("hello")

try:
   print(12 / x)
except ZeroDivisionError:
    print("warning, you are trying to divide by 0")
print()


# Mon erreur a bien été prise en compte !
# Et si j'ai une autre erreur ? Alors j'aurais quand même un message d'erreur, mais il ne sera pas attrapé par le bloc except.

try:
    print(12 / y)  # y n'est pas défini, donc cela va générer une erreur de type NameError
except ZeroDivisionError:
    print("warning, you are trying to divide by 0")
print()

# Nous obtenons ceci dans la console :
# Traceback (most recent call last):
#   File "lesson_19_exception_handling.py", line 77, in <module>
#     print(12 / y)  # y n'est pas défini, donc cela va générer une erreur de type NameError
# NameError: name 'y' is not defined