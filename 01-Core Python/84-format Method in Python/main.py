name = "Alice"
age = 30

# Using format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# You can also specify the position of the placeholders explicitly by using zero-based index numbers inside the curly braces:
formatted_string = "My name is {0} and I am {1} years old.".format(name, age)

# Additionally, you can use named placeholders for more clarity and readability:
formatted_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)

pi = 3.14159
formatted_pi = "The value of pi is {:.2f}".format(pi)
print(formatted_pi)