# Here's an example of passing a function as a parameter in Python:
def greet():
    """This function greets the user."""
    print("Hello!")

def call_function(func):
    """This function calls the given function."""
    print("Calling the function...")
    func()

# Passing the greet function as a parameter to call_function
call_function(greet)