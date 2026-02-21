
# loop

print()
print("for loop")
for i in "tutti quanti":
  print(i)

print()
print("for loop with range")
for i in range(0, 10):
  print(i)

# while loop

print()
print("while loop")
number = 0
while number < 10 :
    number += 1
    print(number)
print('fini !')

print()
print("while loop - multiplication table")
nb = 1
while nb <= 10:
   print(nb, 'x 6 =', nb * 6)
   nb += 1
   

# for loop

print()
print("for loop with range")
for num in range(0, 101):
   print(num)

print()
print("for loop with range and step")
for n in range(4, -1, -2):
   print(n)

# break and continue

print()
print("for loop with break")
for nb in range(5):
   if nb == 3:
      break
   print(nb)

print()
print("for loop with continue")
for nb in range(5):
   if nb == 3:
      continue
   print(nb)

print()
print("while loop with break and continue")
nombre = 0
while nombre < 15 : 
  print(nombre)
  nombre += 1
  if nombre == 5 : 
    break
  continue
  print(1 / 0)
print('fini')

# nested loop

print()
print("nested loop")
for i in range(1, 6):
  for j in range(1, i+1):
    print(j, end=" ") # end=' ' permet de ne pas sauter à la ligne après chaque print
  print() # pour sauter à la ligne après chaque itération de la boucle externe