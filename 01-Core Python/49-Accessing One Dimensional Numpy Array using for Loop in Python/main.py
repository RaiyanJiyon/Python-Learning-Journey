import numpy as np

# Create a one-dimensional NumPy array
my_array = np.array([1, 2, 3, 4, 5])

# Access elements of the array using a for loop
for element in my_array:
    print(element)

# Access elements and their indices using a for loop and enumerate
for index, element in enumerate(my_array):
    print("Index:", index, "Element:", element)