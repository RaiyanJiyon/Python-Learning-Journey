# Numpy One Dimensional Array using logspace Function in Python

You can create a one-dimensional NumPy array with logarithmically spaced values using the numpy.`logspace()` function. This function generates an array of numbers spaced evenly on a log scale over a specified interval.

Here's how you can create a one-dimensional NumPy array using the `numpy.logspace()` function:

```python
import numpy as np

# Create a one-dimensional NumPy array with 10 logarithmically spaced values between 1 and 100
my_array = np.logspace(0, 2, 10)

# Print the array
print(my_array)
```

In this example:

- We first import the NumPy library as `np`.
- We use the `np.logspace()` function to create a one-dimensional NumPy array named `my_array`.
- The function takes `three` arguments
- The starting exponent of the sequence (0 in this case, corresponding to 10**0 = 1).
- The ending exponent of the sequence (2 in this case, corresponding to 10**2 = 100).
- The number of logarithmically spaced values to generate (10 in this case).
- The np.logspace() function generates 10 logarithmically spaced values between 1 and 100 (inclusive) and stores them in the array my_array.
- Finally, we print the array to display the values.


Each value in the array is logarithmically spaced between 1 and 100. The `numpy.logspace()` function is useful when you need a set of values spaced evenly on a logarithmic scale within a specified range.