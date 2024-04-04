'''
In Python, you can return a tuple from a function using the return statement. This allows you to encapsulate multiple values and return them as a single object, which can be useful in various scenarios.

Here's a basic example of a function returning a tuple:
'''

def get_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

# Define a list of numbers
data = [10, 20, 30, 40, 50]

# Call the function and unpack the returned tuple
min_val, max_val, avg_val = get_statistics(data)

print("Minimum:", min_val)
print("Maximum:", max_val)
print("Average:", avg_val)


'''
In this example:

We define a function get_statistics that takes a list of numbers as input.
Inside the function, we calculate the minimum, maximum, and average values of the input list.
We use the return statement to return these values as a tuple (minimum, maximum, average).
We call the get_statistics function with a list of numbers and unpack the returned tuple into separate variables.
Finally, we print the minimum, maximum, and average values.
'''

'''You can return tuples of any size and containing any types of elements from functions in Python. This allows you to encapsulate multiple pieces of data and return them together as a single object.
'''