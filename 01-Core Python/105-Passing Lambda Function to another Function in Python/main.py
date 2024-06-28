# Here's an example of passing a lambda function to another function:
def apply_operation(x, operation):
    """This function applies the given operation to the given value."""
    return operation(x)

# Define a lambda function that squares a number
square = lambda x: x ** 2

# Call the apply_operation function with the lambda function
result = apply_operation(5, square)
print(result)  # Output: 25

# You can also pass lambda functions directly to higher-order functions like map(), filter(), and sorted():
# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using lambda with sorted
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']