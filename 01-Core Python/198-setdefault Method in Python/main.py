my_dict = {'name': 'John', 'age': 30}

# Insert a new key-value pair ('city', 'New York') into the dictionary
city = my_dict.setdefault('city', 'New York')
print("City:", city)  # Output: City: New York

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Retrieve the value for an existing key ('age')
age = my_dict.setdefault('age', 35)  # 'age' key already exists, so no modification is made
print("Age:", age)  # Output: Age: 30