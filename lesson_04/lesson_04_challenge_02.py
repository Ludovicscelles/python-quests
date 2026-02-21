# Challenge_02_lesson_04

# Mission 1 :

# Écrire un programme permettant de calculer la somme des entiers entre 0 et 1000 (tous deux inclus) qui sont divisibles par 2 ou par 5, mais pas par 10.

print()
print("for loop with if and comparison operators")
sum = 0
for number in range(0, 1001):
  if ((number % 2 == 0) or (number % 5 == 0)) and (number % 10 != 0):
    sum += number

print(sum)

# Mission 2 :

#Écrire un programme qui permet de compter le nombre total de chiffres dans un nombre.
#Par exemple le nombre de chiffres pour le nombre 987354 est 6.

print()
print("for loop with string")
number = 987354
number_str= str(number)
count = 0
for n in number_str:
  count +=1
print(count)

# Mission 3 :

# Écrire un programme permettant de calculer la factorielle d'un nombre choisi par l'utilisateur.
# Par exemple, la factorielle de 4 est égale à 4 * 3 * 2 * 1

print()
print("while loop - factorial")
integer = int(input("Saisissez un nombre entier : "))
factorial = 1
n = 1
while n <= integer:
  factorial *= n
  n += 1

print("La factorielle de " + str(integer) + " est de " + str(factorial) + ".")


# Mission 4 :

# Écrire un programme qui permet d'inverser les chiffres d'un nombre.
# Par exemple, 67531 devient 13576

print()
print("while loop - reverse number")
n = int(input("Saisissez un nombre entier : "))
rev = 0

while n > 0:
  d = n % 10
  rev = rev * 10 + d
  n //= 10

print(rev)

# Mission 5 :

# Écrire un programme utilisant une boucle while qui additionne 
# les carrés des nombres entiers (en commençant par 1) tant que la somme reste inférieure ou égale à 300. 
# Une fois que la somme dépasse 300, affichez la somme finale ainsi que le dernier nombre dont le carré a été ajouté.

print()
print("while loop - sum of squares")
number = 1
total = 0

while total <= 300:
  total = total + number**2
  number += 1

print(total)
print(number - 1)

# Mission 6 :

# Écrire un programme qui permet d'afficher la table de multiplication pour tous les nombres entre 1 et 10 (les deux inclus).
# Si le nombre est inférieur ou égale à 5, on souhaite afficher les résultats de ses multiplications par 1 jusqu'à 10.
# Sinon on affiche les résultats de multiplication de ce nombre par 1 à 5

print()
print("nested loop with if")
for i in range (1, 11):
  print("la table de multiplication de ", i)

  if i <= 5:
    limit = 10
  else:
    limit = 5
  
  for j in range (1, limit + 1): 
      print( i * j, end=" ")
  print()


