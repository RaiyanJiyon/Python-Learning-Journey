my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Remove and return an arbitrary (key, value) pair
item = my_dict.popitem()
print("Removed item:", item)  # Output: Removed item: ('city', 'New York')

print(my_dict)  # Output: {'name': 'John', 'age': 30}