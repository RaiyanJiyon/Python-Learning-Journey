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