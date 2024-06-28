# Here's how you can define a function with *args:
def my_function(*args):
    for arg in args:
        print(arg)

# Call the function with multiple arguments
my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello