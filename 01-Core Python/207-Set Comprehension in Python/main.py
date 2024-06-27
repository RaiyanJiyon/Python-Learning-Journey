# Creating a set of squares of numbers from 0 to 9:
squares = {x**2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}


# Creating a set of even numbers from 0 to 9:
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # Output: {0, 2, 4, 6, 8}