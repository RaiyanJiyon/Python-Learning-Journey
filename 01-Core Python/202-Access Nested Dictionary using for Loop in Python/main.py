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