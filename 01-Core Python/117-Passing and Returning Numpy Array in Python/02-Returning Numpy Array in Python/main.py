# Next, let's consider returning a NumPy array from a function:

import numpy as np

def create_array():
    return np.array([1, 2, 3, 4, 5])

# Call the function and store the returned array
result_array = create_array()

print(result_array)  # Output: [1 2 3 4 5]

'''
In this example:

We define a function create_array() that returns a NumPy array [1, 2, 3, 4, 5].
We call the create_array() function and store the returned NumPy array in the variable result_array.
We print the value of result_array, which outputs [1 2 3 4 5].
'''

'''Returning NumPy arrays from functions allows for modularity and code reuse, as you can encapsulate logic for generating or processing arrays within functions and use them in various parts of your code. NumPy arrays provide efficient storage and operations for numerical data, making them ideal for scientific computing and data analysis tasks.
'''