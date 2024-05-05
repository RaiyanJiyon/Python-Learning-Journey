import numpy as np

# Create an array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
arr2 = arr1.view()

# Modify the view
arr2[0] = 10

# Changes are reflected in the original array
print(arr1)  # Output: [10  2  3  4  5]
