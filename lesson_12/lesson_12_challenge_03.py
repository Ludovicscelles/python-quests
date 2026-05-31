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

# Average of a list of numbers: Create a function that returns the average of a list of numbers.

def average(list_num):
    total = 0
    for i in list_num:
      total += i
    
    return total/len(list_num)
   
print(average([15,24,8,85,112]))

# Other way to do it

def average_2(list_num):
   if len(list_num) == 0:
      return 0
   
   return round(sum(list_num) / len(list_num), 2)

print(average_2([15.251, 18.955, 13.212, 27.355]))

# Other way to do it

from statistics import mean

def average_3(list_num):
   return round(mean(list_num), 2)

print(average_3([12.222, 24.895, 52.225]))

# Minimum of a list of numbers: Create a function that returns the minimum from within a list of numbers.

def minimum(list_num):
   return min(list_num)

print(minimum([22, 1, 3, 6, -2, 7]))
print(minimum([25.523, -22.312, 0.128, 10.932]))

# Other way to do it

def minimum_2(list_num):
   
    min_number = list_num[0]

    for i in list_num:
        if i < min_number:
            min_number = i

    return min_number
      
print(minimum_2([1, 4, -5, 0, 2, 6]))
print(minimum_2([-902, -1502, 85.9852, 25.652]))

# Other way to do it: 
        
def minimum_3(list_num):
   
    min_number = list_num[0]
    index = 1

    while index < len(list_num):
      
        if list_num[index] < min_number:
            min_number = list_num[index]
        
        index += 1
    
    return min_number


    
print(minimum_3([-5, -12, -24, 0, 5, 8, 15]))
print(minimum_3([8, 9.25, 9.825, 12, 15, 1.12, 85.98]))

# Maximum of a list of numbers: Create a function that returns the maximum from within a list of numbers.

def maximum(list_num):
   return max(list_num)

print(maximum([-5, 15, 151, 122, 121, 52, -2]))
print(maximum([-12, -52, -12.25, 78.98, 55, 21, 14.78]))

# Other way to do it:

def maximum_2(list_num):

    max_number = list_num[0]

    for i in list_num:
        if i > max_number:
            max_number = i

    return max_number

print(maximum_2([1002, 952, 550, 330, 1350, 1412, 1050]))
print(maximum_2([-501, -512.23, 0.128, -12.152, -330.99]))

# Other way to dot it:

def maximum_3(list_num):

    max_number = list_num[0]
    index = 1

    while index < len(list_num):
        if list_num[index] > max_number:
            max_number = list_num[index]
        index += 1

    return max_number

print(maximum_3([228, 128, 302, 299, 301, 152]))

# Optional Question: Create a function that returns the mode of a list of numbers when more than one modal value is present in a given data set. 
# For example [68, 68, 68, 99, 65, 44, 77, 44, 44] --> [68, 44]

from statistics import multimode

def get_modes(list_num):
    return multimode(list_num)

print(get_modes([68, 68, 68, 99, 65, 44, 77, 44, 44]))

# Other way to do it:

def get_modes_2(list_num):

    counts = []

    for num in list_num:
        counts.append(list_num.count(num))

    max_count = max(counts)


    modes = []

    for num in list_num:

        if list_num.count(num) == max_count:
            modes.append(num)
    
    return modes


print(get_modes_2([15, 12, 12, 11, 10, 8, 15, 8]))
print(get_modes_2([1500, 1600, 1501, 1600, 1499, 1890, 1501]))