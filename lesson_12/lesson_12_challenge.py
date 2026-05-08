# Mission 1: Crate a function, that simply returns the string "Hello Python".

def greeting():
  return "Hello Python"

print(greeting())

# Mission 2: Create a function that takes in 2 numbers as parameters, and returns a boolean indicating whether or not they are equal.

def are_equal(nb1, nb2):
  if nb1 < nb2:
    return False
  elif nb1 > nb2:
    return False
  else:    return True


print(are_equal(5, 5)) # This will return True, because 5 is equal to 5.
print(are_equal(5, 10)) # This will return False, because 5 is not equal to 10.
print(are_equal(10, 5)) # This will return False, because 10 is not equal to 5.

# Other way to do it:

def are_equal(nb1, nb2):
  return nb1 == nb2

print(are_equal(5, 5)) # This will return True, because 5 is equal to 5.
print(are_equal(5, 10)) # This will return False, because 5 is not equal to 10.
print(are_equal(10, 5)) # This will return False, because 10 is not equal to 5.

# Mission 3 : Create a function that takes a number as a parameter, and return the first 10 multiples of the number as a list.

def first_10_multiples(nb):
  multiples = []
  for i in range(1, 11):
    multiples.append(i*nb)
  
  return multiples

print(first_10_multiples(5)) # This will return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], because those are the first 10 multiples of 5.
print(first_10_multiples(3)) # This will return [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], because those are the first 10 multiples of 3.


# Other way to do it:

def first_10_multiples(nb):
  return[i * nb for i in range(1,11)]

print(first_10_multiples(5)) # This will return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], because those are the first 10 multiples of 5.
print(first_10_multiples(3)) # This will return [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], because those are the first 10 multiples of 3.

# Mission 4 : Create a function that takes a string as input, and return its vowels only, preserving case.
# Example: "Antidisestablishmentarianism" will return "Aieaeiaia"
# Example: "TO BE OR NOT TO BE" will return "OOOOTOEE"

def return_vowels(string):
  vowels = "aeiouyAEIOUY"
  vowels_filter = []
  for letters in string:
    if letters in vowels:
      vowels_filter.append(letters)

  return "".join(vowels_filter)

print(return_vowels("LUDOVIC"))

# Other way to do it:

def return_vowels(string):
  vowels = "aeiouyAEIOUY"
  return "".join(letter for letter in string if letter in vowels)

print(return_vowels("HONOLULU"))

# Mission 5 : Create a function that takes 2 numbers as parameters, and return the result of a division operation.
# Test if the denominator is equal to 0 and if so, display a message that says "You can't divide by zero.".

def division(nb1, nb2):
  if nb2 == 0:
    return "You can't divide by 0"
  return nb1 / nb2

print(division(10, 2)) # This will return 5.0, because 10 divided by 2 is 5.
print(division(10, 0)) # This will return "You can't divide by 0", because you can't divide by 0.

# Mission 6 : First, choose two arithmetical operations (such as +, -, *, or /).
# Then, create a function that takes in 3 numbers as parameters and carries out those operations, displays a message that indicating 
# if the result is positive, negative, or zero, and finaly returns the result.
# If a division by zero is attempted, display a error message.

# Example with multiplication and addition:
# Calling with 0, 32, 2 will compute (0 * 32) + 2, will display "Positive result", and return 2.

# Example with division and addition:
# Calling with 21, 0, 3 will try to compute (21 / 0) + 3, will display "Divide-by-zero error", and return None.

def my_operation(num1, num2, num3):
  result = (num1 * num2) - num3

  if result < 0:
   return ("Negative result", result)
  elif result > 0:
    return ("Positive result", result)
  else:
    return ("Result is zero", result)
  
print(my_operation(0, 32, 2)) # This will compute (0 * 32) - 2, will display "Negative result", and return -2.
print(my_operation(21, 0, 3)) # This will compute (21 * 0) - 3, will display "Negative result", and return -3.  
print(my_operation(5, 5, 25)) # This will compute (5 * 5) - 25, will display "Result is zero", and return 0.
print(my_operation(10, 10, 50)) # This will compute (10 * 10) - 50, will display "Positive result", and return 50.
print(my_operation(10, 0, 5)) # This will compute (10 * 0) - 5, will display "Negative result", and return -5.

def my_operation_2(nb1, nb2, nb3):
  if nb2 == 0:
    return "Divide-by-zero error"
  
  result = (nb1 / nb2) - nb3

  if result < 0:
   return ("Negative result", result)
  elif result > 0:
    return ("Positive result", result)
  else:
    return ("Result is zero", result)
  
print(my_operation_2(0, 32, 2)) # This will compute (0 / 32) - 2, will display "Negative result", and return -2.0.
print(my_operation_2(21, 0, 3)) # This will try to compute (21 / 0) - 3, will display "Divide-by-zero error", and return "Divide-by-zero error".  
print(my_operation_2(5, 5, 25)) # This will compute (5 / 5) - 25, will display "Negative result", and return -24.0.
print(my_operation_2(10, 10, 50)) # This will compute (10 / 10) - 50, will display "Negative result", and return -49.0.
print(my_operation_2(10, 2, 5)) # This will compute (10 / 2) - 5, will display "Result is zero", and return 0.0.

# Mission 7 : Create a function that takes a number as a parameter that corresponds to gross salary and returns the net salary for executives.
# You can specify any amount of deduction, or base them on your country's example.

def net_salary(salary):
  return salary * 0.75

print(net_salary(1000)) # This will return 750.0, because the net salary is 75% of the gross salary.
print(net_salary(2000)) # This will return 1500.0, because the net salary is 75% of the gross salary.
print(net_salary(3000)) # This will return 2250.0, because the net salary is 75% of the gross salary.


# Other way to do it:

def executive_net_salary(gross_salary):
  deduction = 0.25
  return gross_salary * (1 - deduction)

print(executive_net_salary(1000)) # This will return 750.0, because the net salary is 75% of the gross salary.
print(executive_net_salary(2000)) # This will return 1500.0, because the net salary is 75% of the gross salary.
print(executive_net_salary(3000)) # This will return 2250.0, because the net salary is 75% of the gross salary.

# Mission 8 : Create a function that can swap the values of two variables,
# such as if variable A = 1 and variable B = 2, after applying the function, variable A = 2 and variable B = 1.

def swap_values(A, B):
  A, B = B, A
  return A, B

print(swap_values(A=1, B=2)) # This will return (2, 1), because the values of A and B have been swapped.

# Other way to do it:

def swap_values_2(A, B):
  temp = A
  A = B
  B = temp
  return A, B

print(swap_values_2(A=1, B=2)) # This will return (2, 1), because the values of A and B have been swapped.