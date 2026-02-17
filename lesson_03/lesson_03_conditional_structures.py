# condition 

x = 10

if x > 5:
  print("La condition est remplie")

if x > 20:
  print("La condition est remplie")


# conditional structure

# if ... else

a = 25

if a > 50:                            # condition (retourne un booléen, True ou False)
  print("La condition est remplie")
else:                                 # ici j'indique ce que je veux faire si la condition n'est pas remplie
  print("La condition n'est pas remplie")

# la condition n'est pas remplie(False), c'est la seconde partie du if qui est exécutée, c'est à dire le else

# Ne pas oublier les deux points : après la condition du if et après le else


# if ... elif ... else

c = 12

if c > 12:                                  # 1ère condition
  print("La condition 1 est remplie.")      
elif c == 12:                               # 2e condition
  print("La condition 2 est remplie.")      
else:                                       # Si aucune des 2 conditions précédentes n'est remplie, on indique quoi faire
  print("Aucune des 2 conditions n'est remplie")


number = 7

# examples

if number > 10:
  print("Tomato")
elif(number != 8):
  print("Banana")
else:
  print("Apple")

# resultat : Banana, car la condition du if n'est pas remplie, mais la condition du elif est remplie (number n'est pas égal à 8)

name = "marie"

if name == "mary":
  print("Ireland")
elif name == "maria":
  print("Colombia")
else:
  print("France")

# resultat : France, car la condition du if n'est pas remplie, et la condition du elif n'est pas remplie non plus, alors c'est le else qui est exécuté

age2 = 21

if age2 < 12:
  print("Kid")
elif age2 >= 12 and age2 < 21:
  print("Teenager")
else:  
  print("Adult")

# resultat : Adult, car la condition du if n'est pas remplie, et la condition du elif n'est pas remplie non plus, alors c'est le else qui est exécuté

age3 = 12

if not(age3 != 12):
  print("Kid")
else:
  print("Other")


# age3 != 12 retourne False, et not False retourne True, alors la condition du if est remplie, et c'est la première partie du if qui est exécutée, c'est à dire le print("Kid")