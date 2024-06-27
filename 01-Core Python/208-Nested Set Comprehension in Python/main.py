# Example 1: Creating a set of tuples where each tuple contains (x, y) pairs
coordinates = {(x, y) for x in range(3) for y in range(2)}
print(coordinates)  # Output: {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)}

# Example 2: Creating a set of squares of numbers from nested lists
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = {num ** 2 for sublist in numbers for num in sublist}
print(squares)  # Output: {1, 4, 9, 16, 25, 36, 49, 64, 81}