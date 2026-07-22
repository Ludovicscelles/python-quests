# You must correct each of the scripts below using exception handling and without modifying lists.

# Script number 1

# list_integers = [1, 12, -45, 6, 27, 0, 24]
# for i in list_integers:
 # print(1/i)

list_integers = [1, 12, -45, 6, 27, 0, 24]
for i in list_integers:
  try:
    print(1/i)
  except ZeroDivisionError:
    print("warning, you're trying to divide by 0.")

print()

# Script number 2

# list_integers = [1, 12, -45, 6, 27, 24]
# for i in range(10):
#   print(1/list_integers[i])

list_integers = [1, 12, -45, 6, 27, 24]
for i in range(10):
  try:
    print(1/list_integers[i])
  except IndexError:
    print("warning, you're trying to access an index outside the list.")

print()

# Script number 3

# list_integers = [1, 12, -45, 6, 27, 0, 24]
# for i in range(10):
#   print(1/list_integers[i])

list_integers = [1, 12, -45, 6, 27, 0, 24]
for i in range(10):
  try:
    print(1/list_integers[i])
  except ZeroDivisionError:
    print("warning, you're trying to divide by 0.")
  except IndexError:
    print("warning, you're trying to access an index outside the list.")

print()

# Script number 4

# list_words = ['hello', 'good morning', 'GOOD Evening', 34, 'Bye' ]
# for word in list_words:
#   print(word.upper())

list_words = ['hello', 'good morning', 'GOOD Evening', 34, 'Bye' ]

for word in list_words:
  try:
    print(word.upper())
  except AttributeError:
    print("warning, this element has no attribute 'upper'.")


