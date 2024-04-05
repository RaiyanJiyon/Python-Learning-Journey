'''
In Python, you can test whether a key exists in a dictionary using various methods. Here are some common ways to do it:
'''

'''
Using the in Keyword:
You can use the in keyword to check if a key exists in a dictionary.
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Check if 'age' exists in my_dict
if 'age' in my_dict:
    print("'age' key exists in my_dict")
else:
    print("'age' key does not exist in my_dict")


'''
Using the get() Method:
The get() method returns the value associated with the specified key. If the key does not exist, it returns None (or a default value if provided), allowing you to handle the case where the key doesn't exist without raising an error.
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Check if 'age' key exists using get()
age_value = my_dict.get('age')
if age_value is not None:
    print("'age' key exists in my_dict")
else:
    print("'age' key does not exist in my_dict")


'''
Using Exception Handling:
You can use exception handling with try-except blocks to handle the case where the key doesn't exist.'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Check if 'age' key exists using exception handling
try:
    age_value = my_dict['age']
    print("'age' key exists in my_dict")
except KeyError:
    print("'age' key does not exist in my_dict")


'''These are some common methods to test whether a key exists in a dictionary in Python. Choose the method that best suits your needs and coding style.'''

