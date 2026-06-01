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