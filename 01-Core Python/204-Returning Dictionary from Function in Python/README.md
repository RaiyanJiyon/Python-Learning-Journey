# Returning Dictionary from Function in Python

Returning a dictionary from a function in Python is a common and useful practice. It allows you to return multiple values in an organized manner. Here's how you can create functions that return dictionaries, along with some examples to illustrate different use cases.

### Basic Example

Here’s a simple function that returns a dictionary containing some basic user information.

```python
def get_user_info():
    user_info = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
    return user_info

user = get_user_info()
print(user)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Function with Parameters

A function that takes parameters and returns a dictionary based on those parameters.

```python
def create_user(name, age, city):
    return {
        'name': name,
        'age': age,
        'city': city
    }

user = create_user('Bob', 25, 'Los Angeles')
print(user)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
```

### Using Calculations

A function that performs some calculations and returns the results in a dictionary.

```python
def calculate_statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return {
        'count': n,
        'mean': mean,
        'variance': variance
    }

stats = calculate_statistics([1, 2, 3, 4, 5])
print(stats)  # Output: {'count': 5, 'mean': 3.0, 'variance': 2.0}
```

### Nested Dictionaries

A function that returns a nested dictionary.

```python
def get_company_info():
    return {
        'company': 'Tech Corp',
        'location': {
            'city': 'San Francisco',
            'state': 'CA'
        },
        'employees': [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25}
        ]
    }

company_info = get_company_info()
print(company_info)
# Output: 
# {
#     'company': 'Tech Corp',
#     'location': {'city': 'San Francisco', 'state': 'CA'},
#     'employees': [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
# }
```

### Combining Data

A function that combines data from multiple sources into a single dictionary.

```python
def combine_data(personal_info, job_info):
    combined_info = {**personal_info, **job_info}
    return combined_info

personal_info = {'name': 'Carol', 'age': 28}
job_info = {'job': 'Engineer', 'company': 'Innovate Ltd'}

combined = combine_data(personal_info, job_info)
print(combined)  # Output: {'name': 'Carol', 'age': 28, 'job': 'Engineer', 'company': 'Innovate Ltd'}
```

### Using Dictionary Comprehensions

A function that uses dictionary comprehensions to construct the return dictionary.

```python
def square_numbers(numbers):
    return {num: num ** 2 for num in numbers}

squares = square_numbers([1, 2, 3, 4, 5])
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Summary

- **Returning a Dictionary**: A useful way to return multiple values from a function.
- **Function with Parameters**: Customize the returned dictionary based on input parameters.
- **Using Calculations**: Perform computations and return the results in a dictionary.
- **Nested Dictionaries**: Organize related data in a hierarchical structure.
- **Combining Data**: Merge data from multiple sources into a single dictionary.
- **Dictionary Comprehensions**: Generate dictionaries in a concise and readable way.

Returning dictionaries from functions allows for flexible and structured data management, making your code more organized and easier to understand.