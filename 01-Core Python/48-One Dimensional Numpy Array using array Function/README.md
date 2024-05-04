# One Dimensional Numpy Array using array Function

To create a one-dimensional NumPy array, you can use the `numpy.array()` function. This function takes a sequence-like object (such as a list or tuple) as input and converts it into a NumPy array. Here's how you can create a one-dimensional NumPy array using the numpy.array() function:

```python
import numpy as np

# Create a one-dimensional NumPy array from a list
my_array = np.array([1, 2, 3, 4, 5])

# Print the array
print(my_array)
```

In this example:

- We first import the NumPy library with the alias np.
- We use the `np.array()` function to create a one-dimensional - NumPy array from a Python list [1, 2, 3, 4, 5].
The resulting array my_array contains the elements [1, 2, 3, 4, 5].

You can also create one-dimensional NumPy arrays from other sequence-like objects, such as tuples:

```python
# Create a one-dimensional NumPy array from a tuple
my_array = np.array((1, 2, 3, 4, 5))

# Print the array
print(my_array)
```

NumPy arrays offer many advantages over Python lists, including better performance for numerical computations, built-in mathematical functions, and more. They are widely used for scientific computing, data analysis, and machine learning tasks in Python.