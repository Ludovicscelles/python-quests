# Mission 9  : Create a function that takes a day as a parameter and return the next day. (i.e. for "Monday" it will return "Tuesday", for "Tuesday" it will return "Wednesday", etc.)
# You can use lists or dictionaries to solve this problem.

def next_day(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day in days:
        index_of_day = days.index(day)
        return days[(index_of_day + 1) % len(days)]
    else: return "Invalid day"

print (next_day("Monday"))
print (next_day("Wednesday"))
print (next_day("Sunday"))
print (next_day("Tuday"))
print("")

def next_day_2(day):
  days = {
    "Monday" : "Tuesday",
    "Tuesday" : "Wednesday",
    "Wednesday" : "Thursday",
    "Thursday" : "Friday",
    "Friday" : "Saturday",
    "Saturday" : "Sunday",
    "Sunday" : "Monday"
  }
  return days.get(day, "Invalid day")


print (next_day_2("Monday"))
print (next_day_2("Thursday"))
print (next_day_2("Sunday"))
print (next_day_2("Sanurday"))

# Mission 10 : Create a function that fills an empty list with values (words) from the following string :
# "After twelve soft showers are the arch-duchess' socks dry, arch-dry?"

words = []

def fill_a_list(string):
   for word in string.split():
      words.append(word)

fill_a_list("After twelve soft showers are the arch-duchess' socks dry, arch-dry?")
print(words)

# Other solution

words_2 = []

def fill_a_list_2(string):
   words_2.extend(string.split())

fill_a_list_2("Once upon a time, in a far away land, a young prince lived in a shining castle.")
print(words_2)


# Mission 11 : Create a function that takes a string as input, converts all characters to lowercase, and returns a new string where
# every vowel at an even index is capitalized, keeping all other characters unchanged. 
# Example: antithetical -> AntithEtIcAl
# Example: marvelously -> marvElOuslY

string = input("Saisissez votre texte : ")

def capitalize_certain_vowels(string):
  
  vowels = "aeiouy"
  result = ""

  for index, letter in enumerate(string.lower()):
    if index % 2 == 0 and letter in vowels:
      result += letter.upper()
    else:
      result += letter
  
  return result

print(capitalize_certain_vowels(string))
      

# Other way to do it

string_2 = input ("Saisissez votre texte : ")

def capitalize_certain_vowels_2(string_2):
   
  vowels = "aeiouy"
  result = []

  for index, letter in enumerate(string_2.lower()):
    if index % 2 == 0 and letter in vowels:
      result.append(letter.upper())
    else:
      result.append(letter)
  
  return "".join(result)


# Mission 12 = Create a function that takes a number n as parameter,
# and return a list containing n lists, each containing n empty lists.


def create_a_grid(n):
   
   return [[[] for j in range(n) ] for i in range(n)]

print(create_a_grid(2))

# Other way to do it :

def create_a_grid_2(n):
   
  grid = []

  for i in range(n):
    row = []

    for j in range(n):
      row.append([])

    grid.append(row)
  
  return grid

print(create_a_grid_2(3))


# Mission 13 : Create a function that takes two inputs, their year of birth and first name.
# Convert the year of birth into an int and subtract it from the current year (you can do it using a certain module : -P)
# Then display the message: Hello [first name], today you are (or you will be this year) [age] years old.
# When testing the function, ask the user for the parameters!

from datetime import datetime

year_of_birth = int(input("What is the year of your birth ? "))
first_name = input("What is your first name ? ")

def display_your_age(year_of_birth, first_name):

  age = (datetime.now().year) - year_of_birth

  return f"Hello {first_name}, today you are (or you will be this year) {age} years old."

print (display_your_age(year_of_birth, first_name))

# Other to do it (without return)

from datetime import datetime

def display_your_age(year_of_birth, first_name):

  age = (datetime.now().year) - year_of_birth
  
  print (f"Hello {first_name}, today you are (or you will be this year) {age} years old.")

year_of_birth = int(input("What is the year of your birth ? "))
first_name = input("What is your first name ? ")

display_your_age(year_of_birth, first_name)