'''
You can also access characters using a while loop by indexing into the string. Here's how you can do it:
'''

my_string = "Hello, World!"

# Using a while loop
index = 0
while index < len(my_string):
    print(my_string[index])
    index += 1

'''In this code:

We define a string my_string.
We use a while loop to iterate over the indices of the string.
Within the loop, we use indexing to access each character of the string using the current index, and we print it.
We increment the index after each iteration to move to the next character.'''