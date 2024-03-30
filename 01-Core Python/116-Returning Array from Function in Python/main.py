'''
In Python, you can return arrays (or lists) from functions just like any other object. You can create, manipulate, and return arrays from functions to achieve various tasks. Here's a basic example of returning an array from a function:
'''

def create_array():
    return [1, 2, 3, 4, 5]

result = create_array()
print(result)  # Output: [1, 2, 3, 4, 5]

'''
In this example:

We define a function create_array() that returns a list [1, 2, 3, 4, 5].
We call the create_array() function and store the returned list in the variable result.
We print the value of result, which outputs [1, 2, 3, 4, 5].
'''

# You can also dynamically generate arrays within functions and return them based on certain conditions or calculations. Here's an example:

def generate_even_numbers(n):
    return [x for x in range(2, n+1, 2)]

result = generate_even_numbers(10)
print(result)  # Output: [2, 4, 6, 8, 10]

'''
In this example:

We define a function generate_even_numbers(n) that generates a list of even numbers up to n.
We use a list comprehension to create the list of even numbers.
We call the generate_even_numbers() function with n = 10 and store the returned list in the variable result.
We print the value of result, which outputs [2, 4, 6, 8, 10].
'''

'''Returning arrays from functions allows for modularity and code reuse, as you can encapsulate logic for generating or processing arrays within functions and use them in various parts of your code.'''