import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Get a slice of the array from index 1 to index 3 (exclusive)
slice1 = my_array[1:4]
print(slice1)  # Output: array('i', [2, 3, 4])

# Get a slice of the array from index 2 to the end
slice2 = my_array[2:]
print(slice2)  # Output: array('i', [3, 4, 5])

# Get a slice of the array from the beginning to index 3 (exclusive)
slice3 = my_array[:4]
print(slice3)  # Output: array('i', [1, 2, 3, 4])

# Get a slice of the array with a step size of 2
slice4 = my_array[::2]
print(slice4)  # Output: array('i', [1, 3, 5])

# Reverse the array using slicing
reverse_array = my_array[::-1]
print(reverse_array)  # Output: array('i', [5, 4, 3, 2, 1])