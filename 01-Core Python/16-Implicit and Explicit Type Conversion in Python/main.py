'''
In Python, type conversion (also known as type casting or type coercion) refers to the process of converting a value from one data type to another. There are two main types of type conversion: implicit and explicit.

Implicit Type Conversion:
Implicit type conversion occurs automatically when the interpreter converts one data type to another without the programmer's intervention. This happens when an operation or expression involving different data types is encountered, and Python automatically converts one or more of the values to a compatible type. Implicit type conversion is also known as automatic type conversion.
'''

# Example of implicit type conversion:
x = 5     # integer
y = 3.14  # float
z = x + y # Implicitly converts x to float, result will be 8.14

'''
Explicit Type Conversion:
Explicit type conversion occurs when the programmer manually converts a value from one data type to another using predefined functions or methods. This is sometimes necessary when you want to ensure that the conversion is done in a specific way, or when Python's implicit type conversion may not produce the desired result.
'''

# Examples of explicit type conversion using built-in functions:
x = 5    # integer
y = "10" # string
z = int(y) + x  # Explicitly converts y to integer, result will be 15

x = 3.14  # float
y = str(x)  # Explicitly converts x to string, result will be '3.14'

'''Explicit type conversion provides more control over the data types used in your program and helps avoid unexpected behavior. However, it's important to handle type conversion carefully to ensure that the converted values are valid and compatible with the intended usage.'''