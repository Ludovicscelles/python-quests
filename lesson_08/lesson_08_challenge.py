# Challenge lesson_07


# Mission 1

# For each cell, execute the code and answer the question before moving on to the next.

people = {"Gontran": 23,
          "Jason": 42,
          "Ayoub": 27}


for i in people:
  print(i)

# 1. What does `i` correspond to?
# To answer, you must use the terms "keys" and "values".

# Answer:

# i corresponds to the keys.

for i in people.keys():
  print(i)

for i in people.values():
  print(i)

# 2. What does i correspond to in the second last cell?
# What does i in the last cell correspond to?

# Answer:

# i corresponds to 42 in the second last cell.
# i correponds to 27 in the last cell.

people = {"Gontran": 23,
          "Jason": 42,
          "Ayoub": 27}

for i in people.items():
  print(i)
  print(type(i))


# 3. What is the type of object returned here called?

# Answer:

# The type of object returned is a tuple.


for i, age in people.items():
  print(age)

for name in people.keys():
  print(name)

# 4. Here I can recover the age of the people. How could I retrieve their names?

# Answer:

# We can retrieve the names by iterating over people.keys().


# Mission 2

people = {"Gontran": 23,
          "Jason": 42,
          "Ayoub": "27",
          "Léo": [10,20,30],
          "Rosario": {"Juan": 3,
                      "Camelia": 6}}


for i in people.values():
  print(type(i))

# 1. Does the above code allow me to confirm that I can have values of different types within a dictionary?

# Answer:


# Yes, there are two integer, a string, a list and a dictionary.


# 2. Can I have kyes of different types within a dictionary?

# Answer:

# Yes

people["Ayoub"] = int(people["Ayoub"])

for i in people.values():
  print(type(i))

print(people.items())

# 3. What did the above code allow me to do?

# Answer:

# Answer:

# The above code allows me to change value type of Ayoub.
# Before, it was a string type and now it's a integer.



# Mission 3

groups = {"groupe_1": ["Lam", "Ghizlaine", "Khaled", "Florian"],
          "groupe_2": ["Lucile", "Mbaye", "Cécile", "Rohan"],
          "groupe_3": ["Agathe", "Charlotte", "Charles", "Maxime"],
          "groupe_4": ["Gaelle", "Linh", "Meral"]}


for i in groups.values():
  print(i)
  print(type(i))

# 1. What is the type of each value?  

# Answer:

# Each value is a list of strings.
# I can iterate through each list to access its elements.

for i in groups.values():
  for v in i:
    print(v)


# 2. How did I get into each list?
# Take the time to explain your reasoning for answering this question.


# Answer:

# First, I iterate over groups.values(), so i becomes each list stored in the dictionary.
# Then, for each list i, I iterate over its elements; v is each string (name) in that list, which I print.
# It's a nested loop: the outer loop goes through the lists, and the inner loop goes through the names in each list.