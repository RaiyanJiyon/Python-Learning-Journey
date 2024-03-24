'''
The format() method in Python is used to format strings by replacing placeholders ({}) with values. This method provides a more flexible and powerful way to format strings compared to C-style formatting. Here's how you can use the format() method:
'''

name = "Alice"
age = 30

# Using format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

'''
In this example:

We define variables name and age.
We use the format() method on the string "My name is {} and I am {} years old.".
Inside the string, {} serves as a placeholder for values to be inserted.
We pass the values of name and age to the format() method as arguments. These values are then inserted into the string in place of the placeholders.
'''

# You can also specify the position of the placeholders explicitly by using zero-based index numbers inside the curly braces:
formatted_string = "My name is {0} and I am {1} years old.".format(name, age)

'''This allows you to reuse the same value multiple times in the string or specify the order of the values differently.'''

# Additionally, you can use named placeholders for more clarity and readability:
formatted_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)

'''
The format() method also supports various formatting options for numbers, such as specifying the number of decimal places, padding with zeros or spaces, alignment, and more. For example:
'''
pi = 3.14159
formatted_pi = "The value of pi is {:.2f}".format(pi)
print(formatted_pi)

'''In this example, :.2f specifies that pi should be formatted as a floating-point number with two decimal places.'''