'''
To access elements of a two-dimensional NumPy array using a while loop in Python, you can use indices to traverse through the rows and columns of the array. Here's how you can do it:
'''


import numpy as np

# Create a two-dimensional NumPy array
two_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the dimensions of the array
num_rows, num_cols = two_dim_array.shape

# Initialize row and column indices
row_index = 0

# Access elements using a while loop
while row_index < num_rows:
    col_index = 0
    while col_index < num_cols:
        print(two_dim_array[row_index, col_index], end=" ")
        col_index += 1
    print()  # Move to the next line after printing each row
    row_index += 1


'''In this code:

We import the NumPy library as np.
We create a two-dimensional NumPy array named two_dim_array.
We get the dimensions of the array using the shape attribute of the array.
We initialize a row index variable row_index to traverse through the rows of the array.
We use nested while loops to traverse through each row and column of the array.
Inside the inner while loop, we access each element of the array using the row and column indices (two_dim_array[row_index, col_index]) and print the element.
After printing all elements in a row, we print an empty line (print()) to move to the next line for the next row.
We increment the row index after printing each row to move to the next row.'''