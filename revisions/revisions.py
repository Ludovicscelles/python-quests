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

# input

name = input("What is your name? ")
print(f"Hello, {name}!")

age = int(input("What is your age? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")

user_information = {
    "name": input("What is your name? "),
    "age": int(input("What is your age? "))
}
print(user_information)

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")

# add another information to the dictionary

user_information["city"] = input("What city do you live in? ")
print(user_information)

# ask the user to enter a position and a new series name, then create a new tuple with the new series name at the specified position

my_tuple_series = ('K2000', 'Hooker', 'Wonder Woman', 'Sherif fais-moi peur', 'MacGyver', 'X-Files', 'Buffy contre les vampires', 'Charmed', 'Smallville', 'Supernatural')
position = int(input("Enter a position (0-9): "))
if 0 <= position < len(my_tuple_series):
    new_tuple_series = my_tuple_series[:position] + (input("Enter a new series name: "),) + my_tuple_series[position:]
    print(new_tuple_series)
else:    print("Invalid position. Please enter a number between 0 and 9.")