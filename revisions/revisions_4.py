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

# is prime number : Create a function that takes a number and returns True if it's a prime number, False otherwise.

def is_prime(nb):

  if nb <= 1:
    return False
  
  for i in range(2, nb):
    if nb % i == 0:
      return False
    
  return True
    
print(is_prime(17))
print(is_prime(18))
print(is_prime(25))

# Other way to do it:

def is_prime_2(nb):

  if nb <= 1:
    return False
  
  for i in range(2, int(nb ** 0.5) + 1):
    if nb % i == 0:
      return False
  
  return True
    
print(is_prime_2(47))
print(is_prime_2(43))
print(is_prime_2(44))

