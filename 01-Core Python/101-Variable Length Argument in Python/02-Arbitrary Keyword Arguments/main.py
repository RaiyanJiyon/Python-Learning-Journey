'''
**Arbitrary Keyword Arguments (kwargs):
Arbitrary keyword arguments (often denoted as **kwargs) allow a function to accept a variable number of keyword arguments. These arguments are passed to the function as a dictionary, where the keys are the argument names and the values are the argument values.
'''

# Here's how you can define a function with **kwargs:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with multiple keyword arguments
my_function(name="Alice", age=30, city="New York")  
# Output:
# name: Alice
# age: 30
# city: New York

'''In this example, the function my_function accepts a variable number of keyword arguments, which are collected into the kwargs dictionary. Inside the function, we iterate over the kwargs dictionary and print each key-value pair.'''