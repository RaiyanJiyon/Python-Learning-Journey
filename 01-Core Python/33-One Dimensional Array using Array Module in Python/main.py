'''
In Python, the array module provides a way to create arrays with elements of a single data type. It offers a more memory-efficient alternative to Python lists for storing homogeneous data. To create a one-dimensional array using the array module, you first need to import the module and then use the array.array() function.
'''

# Here's how you can create a one-dimensional array using the array module:
import array

# Syntax: array.array(typecode, iterable)
# typecode: A single character specifying the type of elements in the array (e.g., 'i' for integers, 'f' for floats)
# iterable: An iterable object (e.g., list, tuple) containing the initial values of the array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the array
print(my_array)

'''In this example:

We first import the array module using import array.
Then, we use the array.array() function to create an array of integers ('i' is the typecode for integers).
The second argument to array.array() is an iterable containing the initial values of the array.'''

# You can also add elements to the array using the append() method:
my_array.append(6)

# And access elements of the array using indexing, just like with lists:
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

'''The array module provides various typecodes to represent different data types, such as integers, floats, characters, and more. Here are some commonly used typecodes:

'b': Signed integer (1 byte)
'B': Unsigned integer (1 byte)
'i': Signed integer (2 bytes)
'I': Unsigned integer (2 bytes)
'f': Float (4 bytes)
'd': Double (8 bytes)
You can choose the appropriate typecode based on the data type of the elements you want to store in the array.'''