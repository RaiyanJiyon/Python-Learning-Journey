'''
Formatted string literals, often referred to as f-strings, provide a convenient way to embed expressions inside string literals for formatting. They were introduced in Python 3.6 and have quickly become the preferred way to format strings due to their simplicity and readability.
'''

# Here's how you can use f-strings in Python:
name = "Alice"
age = 30

# Using f-strings
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)


'''
In f-strings:

The string literal is prefixed with the letter f or F.
Inside the string, expressions enclosed within curly braces {} are evaluated, and their results are inserted into the string.
You can directly reference variables, call functions, and perform any Python expression inside the curly braces.
F-strings support all the usual formatting options, such as specifying the number of decimal places for floating-point numbers, specifying padding, alignment, and more.
'''

# Here are some examples of using f-strings with formatting options:
pi = 3.14159
formatted_pi = f"The value of pi is {pi:.2f}"
print(formatted_pi)

'''
In this example, :.2f specifies that the value of pi should be formatted as a floating-point number with two decimal places.
'''

'''F-strings offer several advantages over other formatting methods:

They are more concise and readable compared to str.format() or % formatting.
They provide better performance.
They offer more flexibility and support for complex expressions directly inside the string.
Overall, f-strings are the recommended way to format strings in modern Python code.'''