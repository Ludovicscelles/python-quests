""" Mathematical functions that need coding
Find x

Now the statisticians are begging you to code ready-made math functions for them. Below are the functions they use most often. Code the functions in the cells below:

Square of a number: Create a function that returns the square of a number.
Cube of a number: Create a function that returns the cube of a number.
Absolute value: Create a function that returns the absolute value of a number.
Factorial of a number: Create a function that returns the factorial of a number.
Mode of a list of numbers: Create a function that returns the mode of a list of numbers, for instance [68, 99, 65, 44, 77, 44, 44] --> 44.
Average of a list of numbers: Create a function that returns the average of a list of numbers.
Minimum of a list of numbers: Create a function that returns the minimum from within a list of numbers.
Maximum of a list of numbers: Create a function that returns the maximum from within a list of numbers.
Yes, all those functions already exist in dedicated modules, and you may not reuse them, unfortunately: you may only use loops, conditionals, basic structures, len, addition, subtraction, multiplication, division and powers.

Don't forget to test your functions with at least two possible cases! """

# Square of a number: Create a function that returns the square of a number.

def square_of_number(n):
    return n ** 2

print(square_of_number(3)) # Output: 9
print(square_of_number(-4)) # Output: 16

# Cube of a number: Create a function that returns the cube of a number.

def cube_of_number(n):
    return n ** 3

print(cube_of_number(2)) # Output: 8
print(cube_of_number(-3)) # Output: -27

# Absolute value: Create a function that returns the absolute value of a number.

def abs_value(n):
    return abs(n)

print(abs_value(-5)) # Output: 5
print(abs_value(7)) # Output: 7

# Factorial of a number: Create a function that returns the factorial of a number.

def factorial(nb):
    
    if nb < 0:
        return "Impossible de calculer le factoriel d'un nombre négatif"
    
    fact = 1

    for num in range(2, nb + 1):
        fact *= num

    return fact

print(factorial(5)) # Output: 120
print(factorial(0)) # Output: 1
print(factorial(-3)) # Output: "Impossible de calculer le factoriel d'un nombre négatif"

# Mode of a list of numbers: Create a function that returns the mode of a list of numbers, for instance [68, 99, 65, 44, 77, 44, 44] --> 44.

def get_mode(list_num):
    
  counts = {}

  for i in list_num:
    if i in counts:
      counts[i] += 1
    else:
      counts[i] = 1

  return max(counts, key=counts.get)

print(get_mode([15, 2, 52, 15, 15, 23, 55, 56, 15]))