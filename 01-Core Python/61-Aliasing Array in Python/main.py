# Here's an example of aliasing an array in Python:
import numpy as np

# Create an array
arr1 = np.array([1, 2, 3, 4, 5])

# Alias the array
arr2 = arr1

# Modify the array through one alias
arr2[0] = 10

# Access the array through the other alias
print(arr1)  # Output: [10  2  3  4  5]