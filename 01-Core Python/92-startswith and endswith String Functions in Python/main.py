string = "Hello, World!"
print(string.startswith("Hello"))  # Output: True
print(string.startswith("World"))  # Output: False


'''
endswith(suffix[, start[, end]]): This method returns True if the string ends with the specified suffix substring, otherwise it returns False. You can also specify optional start and end parameters to specify the slice of the string to consider
'''

print(string.endswith("World!"))  # Output: True
print(string.endswith("Hello"))   # Output: False