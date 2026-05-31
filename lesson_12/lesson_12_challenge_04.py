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