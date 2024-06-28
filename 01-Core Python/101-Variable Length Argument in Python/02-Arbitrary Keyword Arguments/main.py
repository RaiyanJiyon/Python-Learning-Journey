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