'''
In Python, a list is a collection of items, which can be of any data type, such as integers, strings, or even other lists. Lists are mutable, meaning you can modify their elements after they are created. Lists are one of the most versatile and widely used data structures in Python.
'''

# Here's how you can create a list in Python:
# Creating a list of integers
my_list = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "orange"]

# Creating a list with mixed data types
mixed_list = [1, "hello", 3.14, True]

# Creating an empty list
empty_list = []

'''
You can access elements of a list using indexing. Python uses 0-based indexing, meaning the first element of the list has an index of 0, the second element has an index of 1, and so on. Negative indexing is also supported, allowing you to access elements from the end of the list.
'''

# Accessing elements of a list
print(my_list[0])    # Output: 1
print(fruits[1])     # Output: "banana"
print(mixed_list[-1])# Output: True

'''
Lists in Python support various operations such as appending, extending, inserting, removing, and slicing. Here are some common list operations:
'''

# Appending an element to the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Extending the list with another list
fruits.extend(["grape", "pineapple"])
print(fruits)   # Output: ["apple", "banana", "orange", "grape", "pineapple"]

# Inserting an element at a specific index
mixed_list.insert(1, "world")
print(mixed_list)  # Output: [1, "world", "hello", 3.14, True]

# Removing an element from the list
fruits.remove("banana")
print(fruits)   # Output: ["apple", "orange", "grape", "pineapple"]

# Slicing a list
print(my_list[1:4])  # Output: [2, 3, 4]

'''Lists in Python are versatile and powerful data structures that can be used to store and manipulate collections of data in various ways. They are widely used in Python programming for tasks ranging from simple data storage to complex data processing and manipulation.'''