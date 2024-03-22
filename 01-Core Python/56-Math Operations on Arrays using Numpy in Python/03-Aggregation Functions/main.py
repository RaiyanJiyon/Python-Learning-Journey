'''
Aggregation Functions:
NumPy provides functions to compute aggregate statistics of arrays, such as np.sum(), np.mean(), np.max(), np.min(), etc.
'''

import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Compute aggregate statistics
total_sum = np.sum(arr)
mean_value = np.mean(arr)
max_value = np.max(arr)
min_value = np.min(arr)

print("Sum:", total_sum)
print("Mean:", mean_value)
print("Max:", max_value)
print("Min:", min_value)
