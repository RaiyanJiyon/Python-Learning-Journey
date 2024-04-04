'''
Passing a tuple to a function in Python is similar to passing any other type of variable. You can simply include the tuple as an argument when calling the function, and the function can then access and manipulate the tuple as needed.

Here's a basic example of passing a tuple to a function:
'''

def process_tuple(input_tuple):
    for item in input_tuple:
        print(item)

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Call the function and pass the tuple as an argument
process_tuple(my_tuple)


'''
In this example:

We define a function process_tuple that takes a single argument input_tuple.
Inside the function, we iterate over the elements of the input tuple using a for loop and print each element.
We define a tuple my_tuple containing elements (1, 2, 3, 4, 5).
We call the process_tuple function and pass my_tuple as an argument.
'''

'''The function process_tuple receives the tuple as its input_tuple parameter and can perform operations on it as needed. You can pass tuples of any size and containing any types of elements to functions in Python.
'''