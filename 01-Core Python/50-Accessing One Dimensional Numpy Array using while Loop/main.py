import numpy as np

# Create a one-dimensional NumPy array
my_array = np.array([1, 2, 3, 4, 5])

# Get the length of the array
array_length = len(my_array)

# Initialize an index variable
index = 0

# Access elements of the array using a while loop
while index < array_length:
    print(my_array[index])
    index += 1