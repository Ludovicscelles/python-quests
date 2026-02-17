
# loop

for i in "tutti quanti":
  print(i)

for i in range(0, 10):
  print(i)

# while loop

number = 0
while number < 10 :
    number += 1
    print(number)
print('fini !')

nb = 1
while nb <= 10:
   print(nb, 'x 6 =', nb * 6)
   nb += 1
   

# for loop

for num in range(0, 101):
   print(num)

for n in range(4, -1, -2):
   print(n)

# break and continue

for nb in range(5):
   if nb == 3:
      break
   print(nb)

for nb in range(5):
   if nb == 3:
      continue
   print(nb)

print()
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
for i in range(1, 6):
  for j in range(1, i+1):
    print(j, end=' ')
  print()