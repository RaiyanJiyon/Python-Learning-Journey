'''
In Python, the startswith() and endswith() string methods are used to check whether a string starts or ends with a specified substring, respectively. Here's how each method works:
'''

'''
startswith(prefix[, start[, end]]): This method returns True if the string starts with the specified prefix substring, otherwise it returns False. You can also specify optional start and end parameters to specify the slice of the string to consider.
'''

string = "Hello, World!"
print(string.startswith("Hello"))  # Output: True
print(string.startswith("World"))  # Output: False


'''
endswith(suffix[, start[, end]]): This method returns True if the string ends with the specified suffix substring, otherwise it returns False. You can also specify optional start and end parameters to specify the slice of the string to consider
'''

print(string.endswith("World!"))  # Output: True
print(string.endswith("Hello"))   # Output: False

'''These methods are useful for checking whether a string matches certain patterns at the beginning or end. They are often used in conditional statements or boolean expressions to perform specific actions based on the prefix or suffix of a string.'''