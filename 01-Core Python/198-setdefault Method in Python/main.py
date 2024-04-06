'''

In Python, the setdefault() method is used to insert a key-value pair into a dictionary if the specified key is not already present. If the key is already present, the method returns its corresponding value without modifying the dictionary.

The syntax for the setdefault() method is:
'''

# value = my_dict.setdefault(key, default_value)

'''Here's how you can use the setdefault() method:'''

my_dict = {'name': 'John', 'age': 30}

# Insert a new key-value pair ('city', 'New York') into the dictionary
city = my_dict.setdefault('city', 'New York')
print("City:", city)  # Output: City: New York

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Retrieve the value for an existing key ('age')
age = my_dict.setdefault('age', 35)  # 'age' key already exists, so no modification is made
print("Age:", age)  # Output: Age: 30


'''
In this example:

We use the setdefault() method to insert a new key-value pair ('city', 'New York') into the dictionary my_dict. Since the key 'city' is not present in the dictionary, it is added with the specified default value 'New York'.
We then retrieve the value associated with the key 'age' using setdefault(). Since the key 'age' already exists in the dictionary, its existing value 30 is returned, and no modification is made to the dictionary.
'''

'''The setdefault() method is useful when you want to ensure that a key exists in a dictionary and retrieve its corresponding value, optionally providing a default value if the key is not already present.
'''