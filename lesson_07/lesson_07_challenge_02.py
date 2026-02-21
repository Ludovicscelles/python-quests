# Challenge_02 lesson_07

# Preliminary note: sometimes, the challenge tells you to do something that is incompatible with some input (for instance, you ask for a position but the user enters some text, or an invalid number).
# Here you can assume that all user input goes according to plan (the "happy path"). 
# If you want an extra optional challenge, feel free to manage possible error cases!


# Mission 1
# Define a list, then display only the elements (and their position) that have even positions (0, 2, 4, 6...).
# With test_list = ["a", "b", "c", "d", "e"], the script should display:
# a at position 0
# c at position 2
# e at position 4

test_list = ["a", "b", "c", "d", "e"]

# Your code here

print(test_list[0])
print(test_list[2])
print(test_list[4])


# Mission 2
# Define a list, then ask for an index, followed by a string. 
# Then, replace the list element at that index with the given string and display the resulting list.
# For example, with the list test_list2 = ['hello', 'good morning', 'bye bye', 'have a good day'], the index 2, and the string yeah, you should display:
# ['hello', 'good morning', 'yeah', 'have a good day']

test_list = ["hello", "good morning", "bye bye", "have a good day"]

print(test_list)
print()

last_position = len(test_list)-1
print(last_position)

index = int(input("Choisissez l'index en saisissant un nombre entier entre 0 et " + str(last_position) + ":"))
new_value = str(input("Saisissez le nouveau texte : "))

test_list[index] = new_value

print(test_list)
print()


# Mission 3
# Define a list with five numbers, then ask the user for a number. 
# Put the number at the end of the list, remove the first element from the list, and finally display the list.

# For example, with the list test_list3 = [1, 9, 6, 15, 4] and the input 7, you should display:
# [9, 6, 15, 4, 7]

test_list_number_01 = [5, 55, 12, 25, 50, 29, 31]
print(test_list_number_01)
print()

number = int(input("Saisissez un nombre entier : "))
test_list_number_02 = (test_list_number_01.copy()) + [number]
print(test_list_number_02)
print()

test_list_number_03 = test_list_number_02[1:]
print(test_list_number_03)


# Mission 4
# Define a list, then ask the user for a string. 
# Then, insert the string in the list at a random position, and display the resulting list.

# For example, with the list test_list4 = ["p", "y", "t", "h", "o"] and the input n, you might get:
# ["p", "n", "y", "t", "h", "o"]
# ... but you might also get:
# ["p", "y", "t", "n", "h", "o"]

hot_drinks = ["café", "thé", "chocolat chaud", "lait chaud", "tisane", "matcha latte", "chai latte", "cappuccino", "latte macchiato", "americano"]
print(hot_drinks)
print()

new_hot_drink = str(input("Ajoutez votre boisson : "))

import random
random_position = random.randint(0, len(hot_drinks) - 1)

hot_drinks.insert(random_position, new_hot_drink)
print(hot_drinks)


# Mission 5

# Create a list of integers. Then, display a list with the elements ordered from smallest to largest, using the right built-in function.
# With the list test_list5 = [3, 4, 0, -1, 35, 7], this will display:
# [-1, 0, 3, 4, 7, 35]

list_number = [98, 25, 12, 13, -3, -9, 5, 28, 120, 101, 97]

list_ascending_number = sorted(list_number)
print(list_ascending_number)


# Mission 6

# Ask the user for a string, convert it to a list of characters with the list function, then ask for a single character.
# Remove the first occurrence of the character from the list, then display how many occurrences of the character remain in the list.
# For instance if you enter "Excellent work" then the letter "e", it will display:
# There are still 2 copies of e in the list

message_string = str(input("Saisissez message : ")).lower()
print(message_string)
print()


message_list = list(message_string)
print(message_list)
print()

single_character = str(input("Saisissez une lettre de ce message : "))

if single_character in message_list:
  message_list.remove(single_character)

single_character_count = message_list.count(single_character)
print(single_character_count)
print(message_list)
print()

print(f"There are still {single_character_count} copies of {single_character} in the List")


# Mission 7

# Define three lists containing no duplicates. 
# Then, indicate (however you like) the two that have the most elements in common (or all three if there's a tie).

# For instance, with:

# list_a = [1, 2, 4, 8, 16, 32]
# list_b = [1, 2, 3, 5, 8, 13]
# list_c = [2, 3, 5, 7, 11, 13]

# It may display:

# Lists B and C have the most common elements!

list_a = [1, 2, 4, 8, 16, 32]
list_b = [1, 2, 3, 5, 8, 13]
list_c = [2, 3, 5, 7, 11, 13]

commun_elements_ab = set(list_a) & set(list_b)
commun_elements_ac = set(list_a) & set(list_c)
commun_elements_bc = set(list_b) & set(list_c)

commun_elements_count = [len(commun_elements_ab), len(commun_elements_ac), len(commun_elements_bc)]
print(commun_elements_count) 

if max(commun_elements_count) == len(commun_elements_ab):
  print("Lists A and B have the most common elements!")
elif max(commun_elements_count) == len(commun_elements_ac):
  print("Lists A and C have the most common elements!")
else:
  print("Lists B and C have the most common elements!")
