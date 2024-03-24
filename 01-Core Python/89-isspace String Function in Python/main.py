'''
In Python, the isspace() method is used to check whether all characters in a string are whitespace characters. If all characters in the string are whitespace (spaces, tabs, newlines, etc.), the method returns True; otherwise, it returns False
'''

# Here's how you can use the isspace() method:
# Check if all characters are whitespace
whitespace_string = "   \t\n"
print(whitespace_string.isspace())  # Output: True

# Check if any character is non-whitespace
non_whitespace_string = "   Hello   "
print(non_whitespace_string.isspace())  # Output: False

'''In the first example, the string consists only of whitespace characters (' ', '\t', '\n'), so isspace() returns True. In the second example, the string contains non-whitespace characters ('H', 'e', 'l', 'l', 'o'), so isspace() returns False.

The isspace() method is commonly used to validate user input, especially when you expect the input to consist entirely of whitespace characters, such as when checking for empty lines or spaces in text.'''