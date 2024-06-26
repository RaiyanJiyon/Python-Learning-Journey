# isupper(): This method returns True if all characters in the string are uppercase characters, otherwise it returns False.
my_string = "HELLO"
print(my_string.isupper())  # Output: True

my_string = "Hello"
print(my_string.isupper())  # Output: False

# islower(): This method returns True if all characters in the string are lowercase characters, otherwise it returns False
my_string = "hello"
print(my_string.islower())  # Output: True

my_string = "Hello"
print(my_string.islower())  # Output: False

# istitle(): This method returns True if the string is in title case (i.e., if the first character of each word is uppercase and all other characters are lowercase), otherwise it returns False.
my_string = "Hello World"
print(my_string.istitle())  # Output: True

my_string = "Hello world"
print(my_string.istitle())  # Output: False