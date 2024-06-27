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