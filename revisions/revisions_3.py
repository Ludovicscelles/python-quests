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