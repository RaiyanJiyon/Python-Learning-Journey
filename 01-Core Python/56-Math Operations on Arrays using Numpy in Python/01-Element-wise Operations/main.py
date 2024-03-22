'''
ChatGPT
NumPy provides a wide range of mathematical functions and operations that can be performed directly on arrays. Here are some common mathematical operations you can perform on arrays using NumPy:
'''

'''
Element-wise Operations:
You can perform arithmetic operations (addition, subtraction, multiplication, division, etc.) element-wise on arrays. NumPy will apply the operation to each corresponding pair of elements in the arrays.
'''

import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition
result_addition = arr1 + arr2

# Subtraction
result_subtraction = arr1 - arr2

# Multiplication
result_multiplication = arr1 * arr2

# Division
result_division = arr1 / arr2

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
