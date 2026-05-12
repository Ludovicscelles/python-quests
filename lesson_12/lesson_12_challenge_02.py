# Mission 9  : Create a function that takes a day as a parameter and return the next day. (i.e. for "Monday" it will return "Tuesday", for "Tuesday" it will return "Wednesday", etc.)
# You can use lists or dictionaries to solve this problem.

def next_day(day):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  if day in days:
    index = days.index(day)
    return days[(index + 1) % len(days)]
  else:    return "Invalid day"


print(next_day("Monday")) # This will return "Tuesday", because Tuesday is the next day after Monday.
print(next_day("Sunday")) # This will return "Monday", because Monday is the next day after Sunday.
print(next_day("dfqflksqmdj")) # This will return "Invalid day", because "dfqflksqmdj" is not a valid day.


# Other way to do it:

def next_day_2(day):
  days = {
    "Monday": "Tuesday",
    "Tuesday": "Wednesday",
    "Wednesday": "Thursday",
    "Thursday": "Friday",
    "Friday": "Saturday",
    "Saturday": "Sunday",
    "Sunday": "Monday"
  }
  return days.get(day, "Invalid day")

print(next_day_2("Monday")) # This will return "Tuesday", because Tuesday is the next day after Monday.
print(next_day_2("Sunday")) # This will return "Monday", because Monday is the next day after Sunday.
print(next_day_2("dfqflksqmdj")) # This will return "Invalid day", because "dfqflksqmdj" is not a valid day.

# Mission 10 : Create a function that fills an empty list with values (words) from the following string :
# "After twelve soft showers are the arch-duchess' socks dry, arch-dry?"

words = []

def fill_a_list(sentence):
  for word in sentence.split():
    words.append(word)

fill_a_list("After twelve soft showers are the arch-duchess' socks dry, arch-dry?")
print(words) # This will return ['After', 'twelve', 'soft', 'showers', 'are', 'the', "arch-duchess'", 'socks', 'dry,', 'arch-dry?'], because those are the words in the sentence.

# Other way to do it:

words_2 = []

def fill_a_list_2(sentence):
  words_2.extend(sentence.split())
# The extend() method is used to add the elements of a list (or any iterable) to the end of the list. 
# In this case, we are using it to add the words from the sentence to the words_2 list.

fill_a_list_2("After twelve soft showers are the arch-duchess' socks dry, arch-dry?")
print(words_2) # This will return ['After', 'twelve', 'soft', 'showers', 'are', 'the', "arch-duchess'", 'socks', 'dry,', 'arch-dry?'], because those are the words in the sentence. 

# Mission 11 : Create a function that takes a string as input, converts all characters to lowercase, and returns a new string where
# every vowel at an even index is capitalized, keeping all other characters unchanged. 
# Example: antithetical -> AntithEtIcAl
# Example: marvelously -> marvElOuslY

string = input("Saisissez une phrase : ")

def capitalize_certain_vowels(string):
  vowels = "aeiouy"
  result = ""

  for index, letter in enumerate(string.lower()):
    if letter in vowels and index % 2 == 0:
      result += letter.upper()
    else:
      result += letter

  return result


print(capitalize_certain_vowels(string))


# Other way to do it:

string_2 = input("Saisissez une phrase : ")

def capitalize_certain_vowels_2(string):
  vowels = "aeiouy"
  result = []

  for index, letter in enumerate(string.lower()):
    if letter in vowels and index % 2 == 0:
      result.append(letter.upper())
    else:
      result.append(letter)

  return "".join(result)


print(capitalize_certain_vowels_2(string_2))


# Mission 12 = Create a function that takes a number n as parameter,
# and return a list containing n lists, each containing n empty lists.

def create_empty_grid(n):
  return [[[] for j in range(n)] for i in range(n)]

print(create_empty_grid(3)) # This will return [[[], [], []], [[], [], []], [[], [], []]], because it creates a 3x3 grid of empty lists.
print(create_empty_grid(2)) # This will return [[[], []], [[], []]], because it creates a 2x2 grid of empty lists.

# Other way to do it with loops:

def create_empty_grid_2(n):
  grid = []

  for i in range(n):
    row = []

    for j in range(n):
      row.append([])

    grid.append(row)

  return grid

print(create_empty_grid_2(3)) # This will return [[[], [], []], [[], [], []], [[], [], []]], because it creates a 3x3 grid of empty lists.
print(create_empty_grid_2(2)) # This will return [[[], []], [[], []]], because it creates a 2x2 grid of empty lists.


# Mission 13 : Create a function that takes two inputs, their year of birth and first name.
# Convert the year of birth into an int and subtract it from the current year (you can do it using a certain module : -P)
# Then display the message: Hello [first name], today you are (or you will be this year) [age] years old.
# When testing the function, ask the user for the parameters!

from datetime import datetime

year_of_birth = int(input("What is your year of birth? "))
first_name = input("What is your first name? ")

def display_your_age(year_of_birth, first_name):
  current_year = datetime.now().year
  age = current_year - year_of_birth
  return (
    "Hello "
    + first_name
    + ", today you are (or you will be this year) "
    + str(age)
    + " years old."
  )

print(display_your_age(year_of_birth, first_name))

# Other way to do it without return and print (f-string) in the function:

from datetime import datetime

def display_your_age_2(year_of_birth_2, first_name_2):
  current_year = datetime.now().year
  age = current_year - year_of_birth

  print(f"Hello {first_name}, today you are (or you will be this year) {age} years old.")

year_of_birth_2 = int(input("What is your year of birth? "))
first_name_2 = input("What is your first name? ")

display_your_age_2(year_of_birth_2, first_name_2)

