""" Mathematical functions that need coding
Now the statisticians are begging you to code ready-made math functions for them. Below are the functions they use most often. Code the function in the cells below ;-) :

Power of x : Create a function that takes in two numbers as parameters, a number and a power, and returns that number to the indicated power.
Prime number less than x : Create a function that takes a number and returns all the prime numbers that are less than it.
Continuation of Fibonacci : Create a function that takes no parameters, but returns the first 30 numbers in the Fibonnaci sequence.
Square root: Create a function that returns the square root of a number. """

# Power of x : Create a function that takes in two numbers as parameters, a number and a power, and returns that number to the indicated power.

def calculate_power(num, pw):
        return num ** pw

print(calculate_power(2, 2))
print(calculate_power(3, 3))

# Other way to do it:

def calculate_power_2(num, pw):
        return pow(num, pw)

print(calculate_power_2(10, 2))
print(calculate_power_2(9, 4))

# Other way to do it:

def calculate_power_3(num, pw):
        
        result = 1

        for _ in range(pw):
                result *= num

        return result

print(calculate_power_3(2, 3))
print(calculate_power_3(5, 5))


# is prime number : Create a function that takes a number and returns True if it's a prime number, False otherwise.

def is_prime(n):

        if n <= 1:
                return False
        
        for i in range(2, n):
                if n % i == 0:
                        return False
        
        return True

print(is_prime(7))
print(is_prime(8))
print(is_prime(4))


# Other way to do it: 

def is_prime_2(n):

        if n <= 1:
                return False
        
        for i in range(2, int(n ** 0.5) +1):
                if n % i == 0:
                        return False
        
        return True

print(is_prime_2(17))
print(is_prime_2(19))
print(is_prime_2(58))

# Other way to do it: 

def is_prime_3(n):

        if n <= 1:
                return False
        
        return all(
                n % i != 0
                for i in range(2, int(n ** 0.5) + 1)
        )

print(is_prime_3(71))
print(is_prime_3(73))
print(is_prime_3(24))


# Prime number less than x : Create a function that takes a number and returns all the prime numbers that are less than it.

# version 1 - using the is_prime_3 function:

def primes_less_than(n):

        primes = []

        for nb in range(2, n):
                if is_prime_3(nb):
                        primes.append(nb)
        
        return primes

print(primes_less_than(15))
print(primes_less_than(100))

# version 2 - without using the is_prime_3 function:

def primes_less_than_2(n):

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

print(primes_less_than_2(15))
print(primes_less_than_2(100))
        

# Continuation of Fibonacci : Create a function that takes no parameters, but returns the first 30 numbers in the Fibonnaci sequence.

def fibonacci():

        fib = [0, 1]

        for i in range(2, 30):
                fib.append(fib[i - 1] + fib[i - 2])

        return fib

print(fibonacci())

# Other way to do it:

def fibonacci_2():

        fib = [0, 1]

        while len(fib) < 30:
                fib.append(fib[- 1] + fib[- 2])
        
        return fib

print(fibonacci_2())

# Other way to do it:

def fibonacci_3():

        fib = []
        a = 0
        b = 1

        for _ in range(30):
                fib.append(a)

                temp = a + b
                a = b
                b = temp

        return fib

print(fibonacci_3())