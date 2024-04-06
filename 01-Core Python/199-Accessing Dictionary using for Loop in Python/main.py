'''
You can access the key-value pairs in a dictionary using a for loop in Python. When you iterate over a dictionary using a for loop, it iterates over the keys by default. However, you can access both keys and values using the items() method or just the values using the values() method.

Here's how you can access a dictionary using a for loop in Python:
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing keys
print("Accessing keys:")
for key in my_dict:
    print(key)
# Output:
# name
# age
# city

# Accessing keys and values
print("\nAccessing keys and values:")
for key, value in my_dict.items():
    print("Key:", key, "| Value:", value)
# Output:
# Key: name | Value: John
# Key: age | Value: 30
# Key: city | Value: New York

# Accessing values
print("\nAccessing values:")
for value in my_dict.values():
    print(value)
# Output:
# John
# 30
# New York


'''
In the first loop, for key in my_dict:, the loop iterates over the keys of the dictionary. You can access the corresponding values using these keys.

In the second loop, for key, value in my_dict.items():, the items() method is used to iterate over key-value pairs of the dictionary. Inside the loop, key represents the key, and value represents the corresponding value.

In the third loop, for value in my_dict.values():, the values() method is used to iterate over the values of the dictionary. Inside the loop, value represents each value.
'''