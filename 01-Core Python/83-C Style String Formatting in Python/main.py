'''
C-style string formatting in Python can be achieved using the % operator. This method allows you to insert values into a string using format specifiers similar to those used in C's printf() function. Here's how it works:
'''

name = "Alice"
age = 30

# Using C-style string formatting
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

'''
In this example:

%s is a format specifier for a string.
%d is a format specifier for an integer.
The % operator is used to inject the values of name and age into the string formatted_string.
You can use various format specifiers to format different types of data. Here are some common format specifiers:

%s: String (or any object with a string representation, using str()).
%d: Signed decimal integer.
%f: Floating point decimal format.
%x, %X: Hexadecimal integer (lowercase or uppercase).
%o: Octal integer.
%e, %E: Exponential notation (with lowercase or uppercase 'e').
%g, %G: General format (using %f or %e automatically).
You can also specify width, precision, and other formatting options with the format specifiers. For example, %10s specifies a string of width 10, %0.2f specifies a floating point number with two decimal places, etc.
'''

'''
However, the C-style string formatting method is considered somewhat outdated in Python, and the more modern and recommended way to format strings is by using the str.format() method or f-strings (formatted string literals) introduced in Python 3.6. Here's an example using str.format():
'''

# Using str.format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# Or using f-strings:
# Using f-strings
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
