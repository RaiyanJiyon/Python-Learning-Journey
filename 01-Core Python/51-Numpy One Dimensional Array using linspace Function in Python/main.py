'''
In NumPy, you can create a one-dimensional array with equally spaced values using the numpy.linspace() function. This function generates an array of evenly spaced numbers over a specified interval.

Here's how you can create a one-dimensional NumPy array using the numpy.linspace() function:
'''

import numpy as np

# Create a one-dimensional NumPy array with 10 equally spaced values between 0 and 1
my_array = np.linspace(0, 1, 10)

# Print the array
print(my_array)

'''
In this example:

We first import the NumPy library as np.
We use the np.linspace() function to create a one-dimensional NumPy array named my_array.
The function takes three arguments:
The starting value of the sequence (0 in this case).
The ending value of the sequence (1 in this case).
The number of equally spaced values to generate (10 in this case).
The np.linspace() function generates 10 equally spaced values between 0 and 1 (inclusive) and stores them in the array my_array.
Finally, we print the array to display the values.
'''

'''Each value in the array is equally spaced between 0 and 1. The numpy.linspace() function is useful when you need a set of evenly spaced values within a specified range.'''