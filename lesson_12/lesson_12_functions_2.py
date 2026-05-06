# Use a function

amounts_list = [12, 24, 26, 51, 62]

total = 0
for i in amounts_list:
  total += i
print("Total amount is :", total)

# This is the same as:

print("Total amount is :", sum(amounts_list))

# Create a function

""" 
def ma_function(argument):
return something

to call the function, you need to write:
ma_function(argument)
  """

# Arguments

def my_sum(list_argument):
  tot = 0
  for i in list_argument:
    tot += i
  print(tot)

my_sum(amounts_list)

# print(list_argument) # This will not work, because list_argument is only defined inside the function

# print(tot) # This will not work, because tot is only defined inside the function

def substraction(nb, nb_to_substract):
  print(nb - nb_to_substract)

substraction(10, 5)

substraction(nb = 10, nb_to_substract = 5) # You can also specify the name of the arguments when you call the function

substraction(nb_to_substract = 5, nb = 10) # The order of the arguments does not matter when you specify the name of the arguments

substraction(5, 10) # But if you do not specify the name of the arguments, the order matters. Here, nb will be 5 and nb_to_substract will be 10, so the result will be -5.


# Return values

# Instead of printing the result, it is better to use the return statement, so that we can use the result of the function in other parts of the code.

# Insted of this:
def substraction(nb, nb_to_substract):
  print(nb - nb_to_substract)

# We can do this:
def substraction(nb, nb_to_substract):
  return nb - nb_to_substract

# For example, if we do this:

def substraction(nb, nb_to_substract):
  print(nb - nb_to_substract)

# result = substraction(10, 5) + 2
# print(result) # This will not work, because substraction does not return anything, so result will be None, and None + 2 will raise an error.
# A computer doesn't understand how to add something to a print statement, because print does not return anything, it just displays something on the screen.

# But if we do this:

def substraction(nb, nb_to_substract):
  return nb - nb_to_substract 

result = substraction(10, 5) + 2
print(result) # This will work, because substraction returns 5, so result will be 5 + 2, which is 7.


# function with a loop  

def compteur3():
  i = 0
  while i < 3:
    print(i)
    i += 1

print("Bonjour")
compteur3()
compteur3()

# function that call another function

def compteur5():
  i = 0
  while i < 5:
    print(i)
    i += 1

def double_compteur5():
  compteur5()
  compteur5()

print("Bonjour")
double_compteur5()


# Function with a loop and a parameter

def compteur(stop):
  i = 0
  while i < stop:
    print(i)
    i += 1

compteur(3)
compteur(5)

# Function with a loop and a variable as argument

def compteur(stop):
  i = 0
  while i < stop:
    print(i)
    i += 1

a = 10
compteur(a)

# Function with a loop and several parameters

def compteur(start, stop, step):
  i = start
  while i < stop:
    print(i)
    i += step

compteur(0, 10, 2) # This will print 0, 2, 4, 6, 8


# Function and local variables and global variables

def test():
  a = 10 # This is a local variable, it is only defined inside the function
  print(a, b) # This will work, because b is a global variable, it is defined outside the function

a = 5 # This is a global variable, it is defined outside the function
b = 20 # This is a global variable, it is defined outside the function
test() # This will print 10 20, because a is 10 and b is 20. b is a global variable, so it can be accessed inside the function, but a is a local variable, so it cannot be accessed outside the function.
print(a, b) # This will print 5 20, because a is 5 and b is 20. a is a global variable, so it can be accessed outside the function, but the a inside the function is a local variable, so it cannot be accessed outside the function.

# Function with global variable

def test():
  global a # This will tell the computer that we want to use the global variable a, not a local variable
  a = 10 # This will change the value of the global variable a to 10
  print(a, b) # This will print 10 20, because a is now 10 and b is 20

a = 5 # This is a global variable, it is defined outside the function
b = 20 # This is a global variable, it is defined outside the function
test() # This will print 10 20, because a is now 10 and b is 20. a is a global variable, so it can be accessed outside the function, and we have changed its value to 10 inside the function.
print(a, b) # This will print 10 20, because a is now 10 and b is 20. a is a global variable, so it can be accessed outside the function, and we have changed its value to 10 inside the function.

# "True" functions

def cube(x):
  return x ** 3

print(cube(3)) # This will print 27, because 3 to the power of 3 is 27
print(cube(4)) # This will print 64, because 4 to the power of 3 is 64

# Function with a default value for an argument

def formal_greeting(name, title = "Monsieur"):
  print("Veuillez agréer, ", title, name, ", l'expression de mes salutations distinguées.")

formal_greeting("Dupont") # This will print "Veuillez agréer,  Monsieur Dupont , l'expression de mes salutations distinguées.", because we did not specify a title, so it will use the default value "Monsieur"
formal_greeting("Durand", "Mademoiselle") # This will print "Veuillez agréer,  Madame Dupont , l'expression de mes salutations distinguées.", because we specified the title "Mademoiselle", so it will use this value instead of the default value "Monsieur"

# Function with labels for arguments

def bird(voltage=100, state="allumé", action="danser la java"):
  print("Ce peroquet ne pourra pas", action)
  print("si vous le branchez sur", voltage, "volts !")
  print("L'auteur de ceci est complètement", state, ".")

bird() # This will use the default values for all the arguments, so it will print "Ce peroquet ne pourra pas danser la java si vous le branchez sur 100 volts ! L'auteur de ceci est complètement allumé ."
print() # This will print an empty line
bird(state="givré", voltage=250, action="vous approuver") # This will use the values we specified for the arguments, so it will print "Ce peroquet ne pourra pas vous approuver si vous le branchez sur 250 volts ! L'auteur de ceci est complètement givré ."

# Use functions in a script

# We want to calculate the volume of a sphere, which is given by the formula V = (4/3) * pi * r^3, where r is the radius of the sphere. We can use the math module to get the value of pi, but we will use the numpy module instead, because it has a lot of useful functions for scientific computing.

# import numpy as np 
# # This will import the numpy module and give it the alias np, so we can use np.pi to get the value of pi instead of math.pi. 
# We will see more about modules in a later lesson.
import numpy as np

# We can define a function to calculate the cube of a number, which we will use in the formula for the volume of a sphere.
def cube(n):
  return n ** 3

# Now we can define a function to calculate the volume of a sphere, which will use the cube function and the value of pi from the numpy module.
def volume_of_sphere(r):
  return (4/3) * np.pi * cube(r)

# Now we can use this function in a script to ask the user for the radius of the sphere and print the volume of the sphere.
def main():
  r = float(input("Entrez la valeur du rayon de la sphère : "))
  print("Le volume de la sphère est :", volume_of_sphere(r))

# This will only run the main function if this script is run directly, and not if it is imported as a module in another script. 
# This is a common practice in Python to allow code to be reusable as a module, while still allowing it to be run as a standalone script.
if __name__ == "__main__":
  main()