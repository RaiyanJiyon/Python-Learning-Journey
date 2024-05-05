# Math Operations on Arrays using Numpy in Python

NumPy provides a wide range of mathematical functions and operations that can be performed directly on arrays. Here are some common mathematical operations you can perform on arrays using NumPy:

## Element-wise Operations:
You can perform arithmetic operations `(addition, subtraction, multiplication, division, etc.)` element-wise on arrays. NumPy will apply the operation to each corresponding pair of elements in the arrays.

```python
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
```

## Element-wise Functions:
NumPy provides many mathematical functions that can be applied element-wise to arrays, such as `np.sin()`, `np.cos()`, `np.exp()`, `np.sqrt()`, etc.

```python
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
```

## Aggregation Functions:
NumPy provides functions to compute aggregate statistics of arrays, such as `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, etc.

```python
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
```