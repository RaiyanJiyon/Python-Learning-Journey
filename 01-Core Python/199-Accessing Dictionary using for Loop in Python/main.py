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