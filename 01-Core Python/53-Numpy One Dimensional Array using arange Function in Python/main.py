'''
You can create a one-dimensional NumPy array with evenly spaced values using the numpy.arange() function. This function generates an array of numbers within a specified range with a specified step size.

Here's how you can create a one-dimensional NumPy array using the numpy.arange() function:
'''

import numpy as np

# Create a one-dimensional NumPy array with values from 0 to 9 (inclusive)
my_array = np.arange(10)

# Print the array
print(my_array)

'''
In this example:

We first import the NumPy library as np.
We use the np.arange() function to create a one-dimensional NumPy array named my_array.
The function takes one argument: the stop value, which specifies the end of the range of values to generate (10 in this case).
The np.arange() function generates values from 0 up to (but not including) the stop value (10 in this case) with a step size of 1, and stores them in the array my_array.
Finally, we print the array to display the values.
'''

'''Each value in the array is generated with a step size of 1 within the range [0, 10). The numpy.arange() function is useful when you need a sequence of evenly spaced values within a specified range.'''