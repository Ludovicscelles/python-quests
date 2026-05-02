# Lesson 10: Sets in Python
# This is a lesson about sets in Python. A set is an unordered collection of unique elements.

list_of_numbers = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10]
tuple_of_numbers = tuple(list_of_numbers)
set_of_numbers = set(list_of_numbers) # This is how we create a set from a list
print('This is a list:', list_of_numbers)
print('This is a tuple:', tuple_of_numbers)
print('This is a set:', set_of_numbers)
print('Type of the variable set_of_numbers:', type(set_of_numbers))

# Sets are indentified by curly braces {}. 
# Sets automatically remove duplicates, so the set of numbers only contains unique elements.


#  Why are sets useful? They are useful for removing duplicates from a list, and for performing mathematical set operations like union, intersection, and difference.

list_of_values = [24, 55, 19, 71, 42, 48, 37, 25, 74, 17, 65, 72, 91, 70, 47, 50, 15, 48, 27, 60, 67, 3, 20, 82, 57, 9, 76, 70, 89, 19, 93, 26, 85, 87, 0, 15, 80, 23, 78, 78, 33, 36, 31, 72, 57, 0, 40, 28, 56, 8, 62, 78, 95, 31, 51, 39, 0, 14, 73, 75, 60, 38, 97, 21, 43, 44, 17, 23, 79, 69, 10, 95, 73, 8, 30, 70, 43, 2, 7, 30, 68, 59, 79, 4, 50, 96, 19, 90, 23, 67, 15, 85, 27, 61, 10, 15, 62, 64, 30, 36, 11]
print(f'Our list is {len(list_of_values)} values long.')
# With the list of values, we find that there are 101 values in the list, but there are duplicates. We can create a set from this list to find out how many unique values there are.

set_of_values = set(list_of_values)
print(f'Our set is {len(set_of_values)} values long.')
# The set of values is 61 values long, which means there are 61 unique values in the list. We can also find out what those unique values are by printing the set.

# Count methods for sets

# We can also count how many times each unique value appears in the list 
# by creating a dictionary where the keys are the unique values and the values are the counts.
dictionary_for_count = {}
for value in set_of_values:
    # .count() is a method for lists that counts how many times a value appears in the list.
    dictionary_for_count[value] = list_of_values.count(value)
print(dictionary_for_count)


# True and 1 are considered the same value in a set, 
# and False and 0 are also considered the same value. 
# This is because sets are based on the concept of mathematical sets, 
# where each element is either in the set or not in the set, and there is no distinction 
# between different representations of the same value.

# example of this:
thisset = { "apple", "banana", "cherry", True, 1, False, 0 }
print(thisset)
# In this example, the set will only contain "apple", "banana", "cherry", True, and False, 
# because 1 is considered the same as True and 0 is considered

thisset_01 = { "apple", "banana", "cherry", 1, 0, True, False }
print(thisset_01)
# In this example, the set will only contain "apple", "banana", "cherry", 1, and 0, 
# because True is considered the same as 1 and False is considered the same as 0.

# Get the length of a set

# To determine how many unique values are in a set, we can use the len() function, 
# which returns the number of elements in the set.

thisset_02 = { "apple", "banana", "cherry", 1, 0, True, False }
print(len(thisset_02))
# In this example, the length of the set will be 5, because there are 5 unique values 
# in the set: "apple", "banana", "cherry", 1

# Set Items - Data Types

# Set items can be of any data type, and a set can contain different data types.

set1 = { "apple", "banana", "cherry" }
set2 = { 1, 2, 3, 4, 5 }
set3 = { True, False, False, True }

print(set1)
print(set2)
print(set3)

# We can also create a set with mixed data types.

set4 = { "apple", 1, True, 3.14, (1, 2), frozenset({3, 4}) }
print(set4)

# frozenset is a built-in function that creates an immutable set, 
# which means that the elements of the set cannot be changed after it is created.

# type()

# From Python's perspective, sets are defined as objets with the data type 'set'.

my_set = { "apple", "banana", "cherry" }
print(type(my_set))

# From Python's perspective, frozensets are defined as objects with the data type 'frozenset'.
my_frozenset = frozenset({1, 2, 3})
print(type(my_frozenset))

# The set() Constructor

# Using the set() constructor, we can create a set from any iterable, 
# such as a list, tuple, or string.

thisset_03 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset_03)

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
# 1. List is a collection which is ordered and changeable. Allows duplicate members.
# 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3. Set is a collection which is unordered and unindexed. No duplicate members.
# 4. Dictionary is a collection which is ordered and changeable. No duplicate members.

