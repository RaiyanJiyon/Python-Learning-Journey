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