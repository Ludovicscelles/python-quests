# Challenge_02 lesson_07

# Mission 1

# Below is a dictionary containing the number of French campuses that offer each kind of Wild Code School course.
# wildcodeschool = { "data_analyst": 4, "data_scientist": 2, "dev_web": "13" }
# Find a way to only display the keys that have int values.

wildcodeschool =	{
  "data_analyst": 4,
  "data_scientist": 2,
  "dev_web": "13"
}

for key, value in wildcodeschool.items():
  if type(value) == int:
    print(key)

# Mission 2

# For the same dictionary, find a way to display all the values that have a key that contains the letter "e".

wildcodeschool =	{
  "data_analyst": 4,
  "data_scientist": 2,
  "dev_web": "13"
}

for key, value in wildcodeschool.items():
  if "e" in key:
    print(value)


# Mission 3

# Within the same dictionary, change the type of the value of the "dev_web" key to be an int. 
# Then add a new key-value pair which will be "total_campus" : 19, using a dictionary method.

wildcodeschool =	{
  "data_analyst": 4,
  "data_scientist": 2,
  "dev_web": "13"
}
print(type(wildcodeschool["dev_web"]))
wildcodeschool["dev_web"] = int(13)
print(type(wildcodeschool["dev_web"]))

wildcodeschool["total_campus"] = int(19)

print(wildcodeschool)


# Mission 4

# Take the dictionary generated from mission 3. Delete the key value pair :
# 'dev_web': 13 using a method
# 'total_campus': 19 using another method

wildcodeschool =	{
  "data_analyst": 4,
  "data_scientist": 2,
  "dev_web": 13,
  "total_campus" : 19
}

del wildcodeschool["dev_web"]

print(wildcodeschool)

wildcodeschool.pop("total_campus")

print(wildcodeschool)


# Mission 5

# Still within the dictionary generated from Mission 3, find a way to display the dictionary keys in alphabetical order.


wildcodeschool =	{
  "total_campus" : 19,
  "data_analyst": 4,
  "data_scientist": 2,
  "dev_web": 13,
}

for key in sorted(wildcodeschool.keys()):
  print(key)


# Mission 6

# Create a script that returns the same elements as the values() method, as a list.
# Example: for {'a': 1, 'b': 2, 'c': 3} it will create [1, 2, 3]


script = {"a": 1, "b": 2, "c": 3 }

script_list = []

for key, value in script.items():
  script_list.append(value)

print(script_list)
