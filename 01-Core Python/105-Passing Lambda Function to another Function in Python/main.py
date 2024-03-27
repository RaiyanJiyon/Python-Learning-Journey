'''
In Python, you can pass lambda functions as arguments to other functions, just like regular functions. This capability allows for greater flexibility and code reuse, especially when you need to pass simple, one-time-use functions to higher-order functions.
'''


# Here's an example of passing a lambda function to another function:
def apply_operation(x, operation):
    """This function applies the given operation to the given value."""
    return operation(x)

# Define a lambda function that squares a number
square = lambda x: x ** 2

# Call the apply_operation function with the lambda function
result = apply_operation(5, square)
print(result)  # Output: 25

'''
In this example:

We define a function apply_operation() that takes a value x and an operation as arguments. The operation is expected to be a function that takes one argument and returns a result.
We define a lambda function square that squares a number.
We then call the apply_operation() function with arguments 5 and square. The lambda function square is passed as the operation argument.
Inside apply_operation(), the operation function (which is the lambda function square) is called with the value 5, resulting in 5 ** 2 and returning 25.
'''

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

'''In each of these examples, we pass a lambda function directly to the higher-order function without assigning it to a variable first. This allows for concise and readable code when using simple, one-time-use functions.'''
