'''
Element-wise Functions:
NumPy provides many mathematical functions that can be applied element-wise to arrays, such as np.sin(), np.cos(), np.exp(), np.sqrt(), etc.
'''

import numpy as np

# Create an array
arr = np.array([1, 2, 3])

# Apply element-wise functions
result_sin = np.sin(arr)
result_cos = np.cos(arr)
result_exp = np.exp(arr)
result_sqrt = np.sqrt(arr)

print("Sin:", result_sin)
print("Cos:", result_cos)
print("Exp:", result_exp)
print("Sqrt:", result_sqrt)
