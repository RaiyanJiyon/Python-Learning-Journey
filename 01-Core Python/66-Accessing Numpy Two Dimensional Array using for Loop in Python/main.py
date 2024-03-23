'''

To access elements of a two-dimensional NumPy array using a for loop in Python, you can iterate over the rows and columns of the array. Here's how you can do it:
'''
import numpy as np

# Create a two-dimensional NumPy array
two_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access elements using a for loop
for row in two_dim_array:
    for elem in row:
        print(elem, end=" ")
    print()  # Move to the next line after printing each row

'''
In this code:

We import the NumPy library as np.
We create a two-dimensional NumPy array named two_dim_array.
We use a nested for loop to iterate over each row of the array (for row in two_dim_array) and then iterate over each element within the row (for elem in row).
Inside the inner loop, we print each element followed by a space to separate them horizontally.
After printing all elements in a row, we print an empty line (print()) to move to the next line for the next row.
This method allows you to access each element of the two-dimensional array one by one using a for loop.'''

