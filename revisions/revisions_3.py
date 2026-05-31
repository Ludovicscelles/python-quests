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

def square_of_a_number(n):
    return n ** 2

print(square_of_a_number(4))
print(square_of_a_number(-8))

# Other way to do it :

def square_of_a_number_2(n):
    return pow(n, 2)

print(square_of_a_number_2(9))
print(square_of_a_number_2(100))

####

def cube_of_a_number(n):
    return n ** 3

print(cube_of_a_number(2))
print(cube_of_a_number(7))

# Other way to do it :

def cube_of_a_number_2(n):
    return pow(n, 3)

print(cube_of_a_number_2(5))
print(cube_of_a_number_2(-3))

####

def absolute_value(n):
    return abs(n)

print(absolute_value(-128))
print(absolute_value(-15.29))

# Other way to do it:

def absolute_value_2(n):
    if n < 0:
        return -n
    return n

print(absolute_value_2(-15.33))
print(absolute_value_2(7581))

# Other way to do it:

def absolute_value_3(n):
    return -n if n < 0 else n

print(absolute_value_3(-123))
print(absolute_value_3(-12.389))

####

def factorial(n):
    if n < 0:
        return "Impossible de calculer la factorielle d'un nombre négatif"
    
    fact = 1
    for nb in range(2, n + 1):
        fact *= nb
    
    return fact

print(factorial(5))
print(factorial(10))

# Other way to do it:

import math

def factorial_2(n):
    if n < 0:
        return "Impossible de calculer la factorielle d'un nombre négatif"
    return math.factorial(n)

print(factorial_2(5))
print(factorial_2(-10))

# Other way to do it:

def factorial_3(n):
    
    if n < 0:
        return "Impossible de calculer la factorielle d'un nombre négatif"
    
    fact = 1

    while n > 1:
        fact *= n
        n -= 1
    
    return fact

print(factorial_3(4))
print(factorial_3(-2))
print(factorial_3(8))

#####

def get_mode(arr):
    if arr == []:
        return None
    else:
        return max(set(arr), key=arr.count)

print(get_mode([1,7,12,5,6,8,12,9,12]))

# Other way to do it:

def get_mode_2(arr):

    counts = {}

    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
        
    return max(counts, key=counts.get)

print(get_mode_2([1,7,12,5,6,8,12,9,12]))

# Average of a list of numbers: Create a function that returns the average of a list of numbers.

def average(numbers_arr):

    total = 0

    for num in numbers_arr:
        total += num

    return round(total/len(numbers_arr), 2)


print(average([12.52, 15,52, 14.78, 13.1985]))
print(average([0.545464, 5.45456, 4.4565645, 3.6455656]))

# Other way to do it:

def average_2(numbers_arr):
    if len(numbers_arr) == 0:
        return 0
    
    return round(sum(numbers_arr) / len(numbers_arr), 2)

print(average_2([52.4655, 85.64564, 95.456654, 78.4545654]))
print(average_2([5.546456, 5.654546, 5.445654, 5.456456]))

# Other way to do it:

from statistics import mean

def average_3(numbers_arr):
    return round(mean(numbers_arr), 2)

print(average_3([80.5464, 90.44645, 85.45655, 88.4564]))
print(average_3([1.456564, 1.47789897, 1.22366, 1.0465123]))
    
