'''
In Python, anonymous functions, also known as lambda expressions or lambda functions, are small, inline functions defined using the lambda keyword. Lambda expressions are often used when you need a simple function for a short period and don't want to define a full-fledged function using the def keyword.
'''


# Here's the general syntax of a lambda expression:
square = lambda x: x ** 2
print(square(5))  # Output: 25

'''
In this example:

lambda x: x ** 2 defines a lambda function that takes one argument x and returns x ** 2, the square of x.
We assign this lambda function to the variable square.
We then call the square function with an argument 5, which returns 25.
'''

# Lambda expressions are often used with higher-order functions like map(), filter(), and sorted():
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


'''Lambda expressions are concise and often used in situations where defining a regular function would be overkill or when a function is only needed for a short time and doesn't require a descriptive name. However, they should be used judiciously to maintain code readability.'''