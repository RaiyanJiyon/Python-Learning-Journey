# Creating a 2D list of zeros with dimensions 3x3:
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Flattening a 2D list into a 1D list:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]