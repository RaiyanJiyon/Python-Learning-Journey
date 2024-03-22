'''
You can compare NumPy arrays in Python using various comparison operators and NumPy functions. Here's how you can compare NumPy arrays:
'''

'''
Element-wise Comparison:
You can compare elements of two arrays element-wise using comparison operators (<, <=, ==, !=, >, >=). The result of the comparison is a boolean array indicating whether the condition is true for each corresponding pair of elements.
'''

import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

# Element-wise comparison
result_comparison = arr1 == arr2

print("Element-wise Comparison:")
print(result_comparison)  # Output: [False  True False]
