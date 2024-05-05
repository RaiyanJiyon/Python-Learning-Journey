import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

# Element-wise comparison
result_comparison = arr1 == arr2

print("Element-wise Comparison:")
print(result_comparison)  # Output: [False  True False]
