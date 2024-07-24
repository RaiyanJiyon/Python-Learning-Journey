# Create Dictionary using form keys Method in Python

In Python, you can create a dictionary using the fromkeys() method. This method creates a new dictionary with specified keys and a default value for all keys. Here's how you can use it:
'''

## Using fromkeys() method to create a dictionary with default values

```python
keys = ['name', 'age', 'city']
default_value = 'Unknown'

my_dict = dict.fromkeys(keys, default_value)

print(my_dict)
```

In this example:

- We specify a list of keys (keys) and a default value (default_value) to be associated with each key in the new dictionary.
- We call the fromkeys() method on the dict class, passing the keys list and the default_value as arguments.
- The method creates a new dictionary (my_dict) with keys from the keys list and the default value 'Unknown' for all keys.

This is useful when you want to create a dictionary with a predefined set of keys, each initialized with the same default value.