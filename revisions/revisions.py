# Revision

# print("Hello World")  --- IGNORE ---

print("Hello World")

# print indentity 

name = "Ludovic"
age = 45
print(name, age)

# Conditions 

if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")


# Loop

for i in range(5):
    print(i)

print("")

for i in range(1, 6):
    print(i)

# Functions

def greet(name: str) -> str:
    return f"Bonjour {name}!"

print(greet("Ludovic"))


# Lists

my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)
my_list.append(5)
print(my_list)


# Dictionaries

my_dict = {"name": "Ludovic", "age": 45}
print(my_dict)
print(my_dict["name"])
my_dict["age"] = 46
print(my_dict)


# Tuples

my_tuple = (1, 2, 3)
print(my_tuple)
# my_tuple[0] = 10  # This will raise an error because tuples are immutable

my_tuple = (10, 2, 3)  # To change a tuple, you need to create a new one
print(my_tuple)

my_tuple2 = (4, 5, 6)
print(my_tuple + my_tuple2)  # Concatenation of tuples

my_tuple3 = my_tuple + my_tuple2
print(my_tuple3)

my_tuple4 = my_tuple3 * 2  # Repetition of tuples
print(my_tuple4)

my_tuple5 = my_tuple3[1:4]  # Slicing of tuples
print(my_tuple5)

my_tuple6 = my_tuple3[-3:]  # Slicing with negative indices
print(my_tuple6)

my_tuple7 = my_tuple3[::2]  # Slicing with step of 2
print(my_tuple7)