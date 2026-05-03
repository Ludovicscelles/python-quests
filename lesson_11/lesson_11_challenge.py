# Mission 1

"""
Create a function that returns the sum of 3 + 3 when executed.
You must use the return statement.
"""

def add_3_plus_3():
  return 3 + 3

print(add_3_plus_3())


# Mission 2

"""
Create a function that returns the sum of two numbers.
The user of the function must be able to sum two numbers of his choice, when the function is executed.
You must not use input.
"""

def sum_of_two_numbers(a,b):
  return a + b

print(sum_of_two_numbers(15,8))


"""
Question:
What is a parameter in a function?

Answer: 
In Python, a parameter is a variable name listed inside the parentheses of a function definition. It acts as a placeholder for a value that will be passed to the function. An argument is the actual value that is sent to the function when it is called.

"""

# Mission 3

"""
Create a function that returns the sum of two numbers chosen by the user of the function, in a sentence.
For example:
new_sum_2(3,8) returns "The sum of 3 + 8 is equal to 11."
"""

def new_sum_2(number_01, number_02):
  total = number_01 + number_02
  return f"The sum of {number_01} + {number_02} is equal to {total}."

print(new_sum_2(5,25))

# Mission 4

"""
Create a function that returns 2 objects when executed:

 - An object that will be the product of two numbers chosen by the user of the function.
 - A word chosen by the user of the function.

"""

def product_and_word(number1, number2, word):
  total = number1 * number2
  return total, word

print(product_and_word(15,10,"great"))

"""
Your result must be two objects that are in brackets.
This is a tuple.

Question:
Why is the returned object a tuple that contains two objects?

Answer: 
In Python, when a function returns multiple values separated by commas, they are automatically grouped into a tuple. 
That's why the returned object is a tuple containing two objects.

"""

# Mission 5

"""
Create a function that returns the sum of two numbers when executed.
Also, your function must return a sentence that simply indicates if the sum of the two numbers chosen by the user is:

 - less than 10
 - between 10 and 50
 - greater than 50
    
Again, you must use return.

"""

def new_sum_of_two_numbers_2(num01, num02):
  total = num01 + num02

  if total < 10:
    return total, "less than 10"
  elif 10 <= total < 50:
    return total, "between 10 and 50"
  else:
    return total, "greater than 50"

print(new_sum_of_two_numbers_2(2,5))
print(new_sum_of_two_numbers_2(10,2))
print(new_sum_of_two_numbers_2(60,22))