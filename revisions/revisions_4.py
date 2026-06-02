""" Mathematical functions that need coding
Now the statisticians are begging you to code ready-made math functions for them. Below are the functions they use most often. Code the function in the cells below ;-) :

Power of x : Create a function that takes in two numbers as parameters, a number and a power, and returns that number to the indicated power.
Prime number less than x : Create a function that takes a number and returns all the prime numbers that are less than it.
Continuation of Fibonacci : Create a function that takes no parameters, but returns the first 30 numbers in the Fibonnaci sequence.
Square root: Create a function that returns the square root of a number.
"""

# Power of x : Create a function that takes in two numbers as parameters, a number and a power, and returns that number to the indicated power.

def calculate_power(nb, pw):
  return nb ** pw

print(calculate_power(5, 2))
print(calculate_power(3, 3))

# Other way to do it:

def calculate_power_2(nb, pw):
  return pow(nb, pw)

print(calculate_power_2(4, 2))
print(calculate_power_2(5, 3))

# Other way to do it:

def calculate_power_3(nb, pw):
  
  result = 1

  for _ in range(pw):
    result *= nb

  return result

print(calculate_power_3(4, 5))
print(calculate_power_3(5.5, 2))

