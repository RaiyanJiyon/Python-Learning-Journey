'''
In Python, the get() method is used to retrieve the value associated with a specified key in a dictionary. It offers a way to safely access dictionary elements without raising a KeyError if the key does not exist.

The syntax for the get() method is as follows:'''

# value = my_dict.get(key[, default])

'''
key: The key whose value needs to be retrieved.
default (optional): The default value to return if the key is not found in the dictionary. If not provided, None is returned.
Here's how you can use the get() method:
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using get() method to retrieve value associated with 'age' key
age = my_dict.get('age')
print("Age:", age)  # Output: Age: 30

# Using get() method to retrieve value associated with 'salary' key (key not present)
salary = my_dict.get('salary')
print("Salary:", salary)  # Output: Salary: None

# Using get() method with default value
salary_default = my_dict.get('salary', 0)  # Providing a default value of 0
print("Salary (with default):", salary_default)  # Output: Salary (with default): 0

'''
In this example:

We use the get() method to retrieve the value associated with the keys 'age' and 'salary' from the my_dict dictionary.
Since 'age' is present in the dictionary, its corresponding value (30) is returned.
Since 'salary' is not present in the dictionary, the method returns None by default. However, we can specify a default value (0) to be returned if the key is not found.
'''