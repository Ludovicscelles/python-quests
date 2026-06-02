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

# Other way to do it:

def is_prime_3(nb):

  if nb <= 1:
    return False
  
  index = 2

  while index <= int(nb ** 0.5):
    if nb % index == 0:
      return False
    
    index += 1

  return True

print(is_prime_3(23))
print(is_prime_3(29))
print(is_prime_3(28))

# Other way to do it:

def is_prime_4(nb):

  if nb <= 1:
    return False
  
  return all(
    nb % i != 0
    for i in range(2, int(nb ** 0.5) + 1)
  )

print(is_prime_4(83))
print(is_prime_4(84))
print(is_prime_4(89))

# Prime number less than x : Create a function that takes a number and returns all the prime numbers that are less than it.

def prime_less_than(n):

  primes = []

  for nb in range(2, n):
    if is_prime_4(nb):
      primes.append(nb)

  return primes

print(prime_less_than(21))
print(prime_less_than(50))

# Other way to do it:

def prime_less_than_bis(n):

  if n <= 1:
    return []

  primes = []

  for nb in range(2, n):
    if all(
      nb % i != 0
      for i in range(2, int(nb ** 0.5) + 1)
    ):
      primes.append(nb)

  return primes

print(prime_less_than_bis(20))
print(prime_less_than_bis(48))

# Continuation of Fibonacci : Create a function that takes no parameters, but returns the first 30 numbers in the Fibonnaci sequence.

def fibonacci():

  fib = [0, 1]

  for i in range(2, 30):
    fib.append(fib[i - 1] + fib[i -2])

  return fib

print(fibonacci())

# Other way to do it:

def fibonacci_2():

  fib = []
  a = 0
  b = 1

  for _ in range(30):
    fib.append(a)

    temp = a + b
    a = b
    b = temp

  return fib

print(fibonacci_2())

# Other way to do it:

def fibonacci_3():

  fib = [0, 1]
  
  while len(fib) < 30:
    fib.append(fib[-1] + fib[-2])
  
  return fib

print(fibonacci_3())