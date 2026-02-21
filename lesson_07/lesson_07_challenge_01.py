# Challenge lesson_07

# Mission 1

# For each cell, execute the code and answer the question before moving on to the next.

names = ["Fredy", "Nicolas", "Alexandre"]

for i in enumerate(names):
  print(i)
  print(type(i))

# What type of object is returned as output?
# Hint: You can use type(i).

# Answer:

# The type of object returned is a tuple.


for i, val in enumerate(names):
  print(val)

# 2. What does i correspond to?
# What does val correspond to?
# Why is it so?

# Answer:

# i is the index of the current element in the list.
# val is the value of the current element in the list.


for val, i in enumerate(names):
  print(i)

# 3. This time, i returns first names and val returns numbers. Why is it so?

# Answer:

# Because enumerate() always returns a tuple (index, value), 
# Python assigns them by position. In the second loop, the variables are reversed, so val receives the index and i receives the name.

# 4. What does the built in function enumerate do? In what cases can it be useful?

# Answer:

# The function enumenrate() add a counter to an iterable object such a list. 
# It simpliflies looping by returning pairs of (index, value).


# Mission 2

test_list = ['Hi', 'my', 'name', 'is', "hi", "my","name", "is", "chickychicky"]

test_list[8] = "Marshall"

test_list

# What does the 8 in square brackets mean?
# What action has been performed?

# Answer:

# The 8 in square brackets refers to index 8 of the list.
# The action performed is to change the value at index 8 from "chickychicky" to "Marshall".


test_list = ['Hi', 'my', 'name', 'is', "hi", "my","name", "is", "Marshall"]

for i in range(4):
  print(test_list[i])

# What does range(4) mean?
# Why are only the first 4 elements of test_list displayed?

# Answer:

# range(4) returns the numbers from 0 to 3 because the single argument specifies the upper limit of the loop.


print(test_list)
for i in range(2, 8, 2):
  print(test_list[i])

# 3. What does range(2, 8, 2) mean ?
# Why are only the elements 'name', 'hi' and 'name' displayed?

# Answer:

# range(2, 8, 2) starts at 2, increments by 2, and stops before 8, producing sequence 2, 4, 6.



# Mission 3

numbers = [2,3,1,5,9]

for i in range(10,15):
  numbers.append(i)

numbers


# 1. What does range(10,15) mean ?
# What is the purpose of the method append() ?

# Answer:

# range(10, 15) define a sequence from 10 to 15 (15 is exclude).
# The purpose of the methode append() is to add numbers in numbers list.

# 2. What is the purpose of the del command?

# The purpose of the del command is to remove the last of the list or to delete a variable.



# Mission 4

import random

random.randint(0,10)

# 1. What can the method randint() do ?

# Answer:

# randint() returns a random integer within the given range.



# 2. What can the method .insert() do ?
# You must answer using the terms 'parameter' and 'argument'.

# Answer:

# .insert() adds a value into a list at a specific index. The index and the value are given as arguments.



# Mission 5


test_list = ['Hi', 'my', 'name', 'is', "hi", "my","name", "is", "chickychicky"]

print(type(test_list))

test_list = " ".join(test_list)

test_list

print(type(test_list))

# 1. What can the .join() method do?
# What is the type of test_list before using .join()?
# What is the type of test_list after using .join()?

# Answer:

# The .join() method concatenates elements of a sequence such as a list or a tuple into a single string.
# Before using .join(), type of test_list is list.
# After using .joint(), type of test_list is string.


christmas = "Noël c'est bien, mais attention à ne pas manger trop de chocolat. On le sait, mais on le fais à chaque fois. C'est la vie"
print(type(christmas))
print(christmas)
new_christmas = christmas.split()
print(type(new_christmas))
print(new_christmas)

# 2. What can the .split() method do?
# What is the type of christmas before using .split()?
# What is the type of christmas after using .split()?

# Answer:

# The .split() method divides a string into a list of substrings using a separator.
# By default, the sperator is a space.
# Before using .split(), type of christmas is string.
# After using .split(), type of christmas is list.


christmas = "Noël c'est bien, mais attention à ne pas manger trop de chocolat. On le sait, mais on le fait à chaque fois. C'est la vie"


christmas.split("à")


# 3. Why does the .split() method split the string into 3 elements?

# Answer:

# Because .split() method is used with "à" as separator and the string contains 2 "à", so it splits the string into 3 parts: before the first "à", between the two "à", and after the second "à".
