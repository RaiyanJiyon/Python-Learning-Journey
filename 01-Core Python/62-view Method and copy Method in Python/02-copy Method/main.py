import numpy as np

# Create an array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a copy of the original array
arr2 = arr1.copy()

# Modify the copy
arr2[0] = 10

# Changes are not reflected in the original array
print(arr1)  # Output: [1 2 3 4 5]