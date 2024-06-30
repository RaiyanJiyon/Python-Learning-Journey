# Here's how you can create and execute an IIFE in Python:

# Define and call the IIFE
(lambda x: print(x))(10)  # Output: 10

# Alternatively, you can use a regular named function for more complex IIFEs:

# Define a function and immediately call it
def my_iife(x):
    print(x)

my_iife(10)  # Output: 10