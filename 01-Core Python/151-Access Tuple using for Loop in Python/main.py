'''
You can access elements of a tuple using a for loop in Python, just like you would with other iterable objects such as lists. Here's how you can iterate over a tuple using a for loop:
'''

my_tuple = (1, 2, 3, 'hello')

# Accessing elements of a tuple using a for loop
for element in my_tuple:
    print(element)


'''
In this example:

We have a tuple my_tuple containing elements (1, 2, 3, 'hello').
We use a for loop to iterate over each element of the tuple.
During each iteration, the variable element takes on the value of each element in the tuple, one at a time.
Inside the loop, we print each element.
This loop will iterate over each element of the tuple in order, from the first element to the last. It's a convenient way to process each element of a tuple without needing to manually index each element.
'''