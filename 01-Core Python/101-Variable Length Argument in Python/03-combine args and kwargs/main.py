'''
You can also combine *args and **kwargs in the same function definition to accept both positional and keyword arguments:
'''

def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with both positional and keyword arguments
my_function(1, 2, 3, name="Alice", age=30)  
# Output:
# 1
# 2
# 3
# name: Alice
# age: 30
