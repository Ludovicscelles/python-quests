# Challenge lesson_06

#  Mission 1

# What's the lenght of the following string ?

s = "Taumata whakatangihanga koauau o tamatea turi pukaka piki maungah oronuku pokai whenuaki tanatahu"

len(s)

# Mission 2 

# Ask the user for a string, then for a character (we assume user input follows the rules). 
# Then, display the positions, starting with 1, of all occurrences of the character within the string.
# For example, for the word "welcome" and for the character "e", the script will display:
  
  # position: 2
  # position: 7

word = str(input("Saisissez un mot : "))
character = str(input("Choisissez une lettre de ce mot : "))

for i in range (len(word)):
  if word[i] == character:
    print("position:",i + 1)

# Mission 3

# Ask the user for a string, then for an integer. 
# Then, display the string repeated as many times as the given integer.
# For example, badger and 4 will display badgerbadgerbadgerbadger

phrase = str(input("Saisissez une phrase : "))
number = int(input("Saisissez un nombre entier : "))
print(phrase*number)


# Mission 4

# Display the following string without including the spaces at the beginning and end. 
# There's a string method that does exactly that, look at the documentation!

s = "   Data Analyst    "
s_without_spaces = s.strip()
print(len(s))
print(len(s_without_spaces))


# Mission 5

# Ask the user for a string, then for a character, then for another character.
# Then, display the string where the occurences of the first character are replaced by the second one.
# For example:

# string = "Boulgour"
# 1st_char = "g"
# 2nd_char = "v"
# Result : "Boulvour"


word = str(input("Saisissez un mot : "))
first_char = str(input("Saisissez une lettre de ce mot : "))
second_char = str(input("Saisissez une lettre : "))
new_word = word.replace(first_char, second_char)
print(new_word)


# Mission 6
# Ask the user for a string. Then, display the same string with all vowels converted to uppercase, and all consonants converted to lowercase.
# For example:

# string = "Papa's got a brand new bag"
# Result : "pApA's gOt A brAnd nEw bAg"

phrase = str(input('Saisissez votre phrase : ')).lower()

for i in range(len(phrase)):
  if phrase[i] in ["a", "e", "i", "o", "u"]:
    phrase = phrase[:i] + phrase[i].upper() + phrase[i+1:]


print(phrase)