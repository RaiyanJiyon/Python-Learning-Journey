'''
You can pass a dictionary as an argument to a function in Python just like any other object. This allows you to operate on the dictionary within the function's scope.

Here's an example of how to pass a dictionary to a function:
'''

# Define a function that takes a dictionary as an argument
def process_dictionary(input_dict):
    for key, value in input_dict.items():
        print(key + ":", value)

# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Call the function and pass the dictionary as an argument
process_dictionary(my_dict)


'''
In this example:

We define a function process_dictionary() that takes a single argument input_dict, which is expected to be a dictionary.
We create a dictionary my_dict.
We call the process_dictionary() function and pass my_dict as an argument.
Inside the function, we iterate over the items of the dictionary and print each key-value pair.
The function can then operate on the dictionary just like any other object, allowing you to perform various operations on it within the function's scope.
'''