'''
Array-wise Comparison:
You can compare entire arrays using NumPy functions such as np.array_equal() or np.all(). The np.array_equal() function returns True if two arrays have the same shape and elements, while np.all() returns True if all elements in the boolean array are True.
'''

import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

# Array-wise comparison
result_array_equal = np.array_equal(arr1, arr2)
result_all = np.all(arr1 == arr2)

print("Array-wise Comparison:")
print("np.array_equal:", result_array_equal)  # Output: True
print("np.all:", result_all)  # Output: True
