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