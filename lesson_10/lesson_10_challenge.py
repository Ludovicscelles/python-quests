# There is another object type we haven't talked about: set
# It looks like a dictionary, but it's not a dictionary.

my_set = {"apple", "kiwi", "pineapple"}
type(my_set)

# Question : Why isn't my_set an object from the dict class ?

# Answer : my_set isn't an object from the dict class because there no key/value pairs like dictionaries, there are only values separated by commas, which defines a set in Python.

# Another specificity from set object is that they cannot have two items with the same values.

# Execute the cells below.

a_set = {"banana", "lemon", "lemon", "cherry", "lemon", "strawberry", "lemon" }
print(a_set)


# Question :

# How many items do the sets below have ?

# To answer, you can use your knowledge or the len() function.

this_set = {1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9}
len(this_set)

# There are 9 unique items.

# Question :

# Can a set contain elements with differents types ?

# Yes, a set can contain elements of differents types, as long they are hashable (e.g., numbers, strings, tuples)

# try to make a set with objects with different types here:
answer = {"hey", 2, True, 2.33}

# Double-click (or enter) to edit

# Question :

# Using the list below, there is a simple way to know the amount of unique values from this list.

# What is it ?

# Answer :

# To know the amount of unique values in this list, we convert it into a set and print its length.

# Try to count the amount of unique values from this list, in one line of code.

a_list = [1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9]
print((len(a_list)))

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members, but you can remove items and add new items.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

# Question :
# Find a way to access to the first value of this_set

this_set = {1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9}
print(list(this_set)[0])

# Question :
# Find a way to add a value that will be unique in a_set

a_set = {"banana", "lemon", "lemon", "cherry", "lemon", "strawberry", "lemon" }
a_set.add("orange")
print(a_set)

# Question :
# Now, you have to add the value from this_set to a_set:

# Double-click (or enter) to edit

this_set = {1, 2, 3, 1, 2, 4, 1, 4, 3, 5, 6, 8, 9, 8, 3, 7, 6, 8, 6, 8, 9}
a_set = {"orange", "banana", "lemon", "lemon", "cherry", "lemon", "strawberry", "lemon" }
a_set.update(this_set)
print(a_set)


# Question :

# If you display a set object, it won't display with the same order you define it.

# What can you say about the order the element are display ?

# Answer : In a set, items do not have a defined order. Set items can appear in a different order every time we use them and cannot be reffered by an index or a key.

# Question :

# Find a way to display the elements that exist in both sets.

a_set = {"banana", "grapes", "cherry", "pineapple", "kiwi", "strawberry"}

b_set = {"lemon", "kiwi", "grapes", "blueberry", "watermelon"}

print(a_set & b_set)