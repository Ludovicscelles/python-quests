# Mission 1
# Create a tuple of your choice containing 10 elements in this order:

# 3 integers
# 3 strings
# 2 lists containing 3 items each
# 2 dictionaries containing 3 items (3 key/value pairs) each

tuple1 = (10,20,30, 'abc', 'def', 'ghi', ['apple', 'banana', 'strawberry'], [5030, 1450, 1890], {'Ludo': 45, 'Nathan': 48, 'Theo': 42}, {'Helena': 52, 'Anastacia': 58, 'Johanna': 41} )

# Now, access the second-to-last item in the second list.

print(tuple1[7][-2])

# Mission 2

# In the same tuple, access the last 4 elements using slicing.

print(tuple1[-4:])

# Mission 3

# Change the value of the 4th element (the first string) of your tuple (since tuples are immutable, this means recreating a tuple where this element is changed).

tuple1 = tuple1[:3] + ('cba',) + tuple1[-6:]
print(tuple1)

# Mission 4

# Create 2 tuples of the same length that contain only integers.

# Then create a script that compares the sum of their elements and displays the tuple that has the highest total.

tuple2 = (28, 49, 52)
tuple3 = (88, 22, 41)

if sum(tuple2) > sum(tuple3):
    print(tuple2)
elif sum(tuple2) < sum(tuple3):
    print(tuple3)
else:    print("The sums of the two tuples are equal.")

# Mission 5 

# Here's a tuple:

# my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")

# Ask the user for a string, then for an integer position. 
# Create an altered copy of my_tuple where the element at the given position is now the given string.

my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")

new_data_type = input("Entrer une nouvelle spécialité de data: ")
integer_position = int(input("Entrer une position: "))

if 0 <= integer_position < len(my_tuple):
  my_tuple = my_tuple[:integer_position] + (new_data_type,) + my_tuple[integer_position +1:]
  print(my_tuple)
else: 
  print(f"La position n'est pas valide. Merci d'entrer un nombre entre 0 et {len(my_tuple)-1}.")