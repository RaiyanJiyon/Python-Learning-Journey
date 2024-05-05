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
