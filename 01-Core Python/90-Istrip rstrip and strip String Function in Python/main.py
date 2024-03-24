'''
In Python, the strip(), lstrip(), and rstrip() methods are used to remove leading and trailing whitespace characters (spaces, tabs, newlines) from a string. Here's how each method works:
'''

# strip(): This method removes leading and trailing whitespace characters from both ends of the string.

string = "   Hello, World!   "
print(string.strip())  # Output: "Hello, World!"

# lstrip(): This method removes leading whitespace characters from the left end (beginning) of the string.
string = "   Hello, World!   "
print(string.lstrip())  # Output: "Hello, World!   "

# rstrip(): This method removes trailing whitespace characters from the right end (end) of the string.
string = "   Hello, World!   "
print(string.rstrip())  # Output: "   Hello, World!"

'''
These methods are useful for cleaning up input strings, especially when working with user input or reading text from files where leading and trailing whitespace may be present. Additionally, you can provide an optional argument to these methods to specify the characters that should be removed instead of whitespace. For example:
'''
string = "###Hello, World!###"
print(string.strip("#"))  # Output: "Hello, World!"

'''This removes leading and trailing # characters from the string.'''