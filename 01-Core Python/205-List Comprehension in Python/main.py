# Creating a list of squares of numbers from 0 to 9:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Creating a list of even numbers from 0 to 9:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


# Creating a list of characters in a string:
string = "hello"
chars = [char for char in string]
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']