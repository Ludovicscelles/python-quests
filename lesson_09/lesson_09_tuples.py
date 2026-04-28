# Tuples are immutable, meaning that once they are created, their elements cannot be changed.
# Lists are mutable, meaning that their elements can be changed after they are created.

list = [ 'apple', 'banana', 'cherry' ]
print(list[1])  # Output: banana

print (list[2])  # Output: cherry

list[1] = 'blueberry'
print(list)  # Output: ['apple', 'blueberry', 'cherry']
print(len(list))  # Output: 3

tuple = ( 'apple', 'banana', 'cherry' )
print(tuple[1])  # Output: banana

# tuple[1] = 'blueberry'  # This will raise a TypeError because tuples are immutable


