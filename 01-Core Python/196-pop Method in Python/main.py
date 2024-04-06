'''
In Python, the pop() method is used to remove and return the value associated with a specified key in a dictionary. If the key is not found, it raises a KeyError unless a default value is provided.

The syntax for the pop() method is as follows:
'''

# value = my_dict.pop(key[, default])

'''
key: The key whose value needs to be removed.
default (optional): The default value to return if the key is not found in the dictionary. If not provided and the key is not found, a KeyError is raised.
'''

# Here's how you can use the pop() method:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Remove and return the value associated with the 'age' key
age = my_dict.pop('age')
print("Age:", age)  # Output: Age: 30

# Remove and return the value associated with the 'salary' key (key not present)
try:
    salary = my_dict.pop('salary')
    print("Salary:", salary)
except KeyError as e:
    print("KeyError:", e)  # Output: KeyError: 'salary'

# Remove and return the value associated with the 'salary' key with default value
salary_default = my_dict.pop('salary', 0)  # Providing a default value of 0
print("Salary (with default):", salary_default)  # Output: Salary (with default): 0

print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}


'''
In this example:

We use the pop() method to remove and return the value associated with the keys 'age' and 'salary' from the my_dict dictionary.
Since 'age' is present in the dictionary, its corresponding value (30) is returned, and the key-value pair is removed from the dictionary.
Since 'salary' is not present in the dictionary and no default value is provided, the method raises a KeyError. However, we handle this case using a try-except block.
We can also provide a default value to be returned if the key is not found, as demonstrated with the 'salary' key.
After the pop() operations, the dictionary is modified accordingly.
'''