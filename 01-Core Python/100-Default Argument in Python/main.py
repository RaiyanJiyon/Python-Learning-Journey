# Here's an example of using default arguments in a function:
def greet(name, greeting="Hello"):
    """This function greets the person with the given name using the provided greeting."""
    print(f"{greeting}, {name}!")

# Call the greet function with only the required argument
greet("Alice")  # Output: Hello, Alice!

# Call the greet function with both arguments
greet("Bob", "Hi")  # Output: Hi, Bob!