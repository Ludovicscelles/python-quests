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