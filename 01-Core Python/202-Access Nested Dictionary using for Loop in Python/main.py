'''
You can access the elements of a nested dictionary using a for loop in Python. To iterate through a nested dictionary, you typically need nested loops to access the keys and values of each level of the dictionary hierarchy.

Here's how you can access a nested dictionary using a for loop:
'''

nested_dict = {
    'person1': {'name': 'John', 'age': 30, 'city': 'New York'},
    'person2': {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
}

# Accessing nested dictionary using a for loop
for person, details in nested_dict.items():
    print("Details of", person)
    for key, value in details.items():
        print(key + ":", value)
    print()


'''
In this example:

The outer loop iterates over the items of the nested_dict dictionary, giving us the key-value pairs where the value is itself a dictionary.
Inside the outer loop, we have another loop that iterates over the key-value pairs of each inner dictionary (details).
We print each key and value pair, giving us the details of each person in the nested dictionary.
This approach allows you to access and print or process each element of the nested dictionary in a structured manner.
'''