# Here's an example demonstrating the usage of the index() method:
my_list = [1, 2, 3, 4, 3, 5]

# Find the index of the first occurrence of the value 3
index = my_list.index(3)
print("Index of value 3:", index)  # Output: Index of value 3: 2

my_list = [1, 2, 4, 5]

# Attempt to find the index of the value 3 (which does not exist in the list)
try:
    index = my_list.index(3)
    print("Index of value 3:", index)
except ValueError:
    print("Value not found in the list")