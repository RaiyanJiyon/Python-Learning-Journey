# Nested Dictionary in Python

In Python, a nested dictionary is a dictionary that contains one or more dictionaries as its values. This allows for hierarchical and structured data representation, suitable for modeling complex relationships and data organization. Here's how you can define, access, and manipulate nested dictionaries in Python:

### Definition of a Nested Dictionary

A nested dictionary consists of key-value pairs where the values are themselves dictionaries. Here's an example:

```python
employees = {
    'emp1': {
        'name': 'Alice',
        'age': 30,
        'department': 'HR'
    },
    'emp2': {
        'name': 'Bob',
        'age': 25,
        'department': 'IT'
    },
    'emp3': {
        'name': 'Carol',
        'age': 28,
        'department': 'Finance'
    }
}
```

In this example:
- `employees` is a dictionary where each key (`'emp1'`, `'emp2'`, `'emp3'`) maps to another dictionary containing employee details (`'name'`, `'age'`, `'department'`).

### Accessing Values in Nested Dictionary

You can access values in a nested dictionary by chaining keys together, similar to accessing nested lists or other nested data structures:

```python
# Accessing specific employee details
print(employees['emp1']['name'])  # Output: Alice
print(employees['emp2']['age'])   # Output: 25
print(employees['emp3']['department'])  # Output: Finance
```

### Modifying Values in Nested Dictionary

You can modify values in a nested dictionary using assignment:

```python
# Updating employee details
employees['emp1']['age'] = 32
employees['emp2']['department'] = 'Engineering'

print(employees['emp1'])  # Output: {'name': 'Alice', 'age': 32, 'department': 'HR'}
print(employees['emp2'])  # Output: {'name': 'Bob', 'age': 25, 'department': 'Engineering'}
```

### Adding New Entries

You can add new entries to a nested dictionary by assigning values to new keys:

```python
# Adding a new employee
employees['emp4'] = {'name': 'David', 'age': 35, 'department': 'Marketing'}

print(employees['emp4'])  # Output: {'name': 'David', 'age': 35, 'department': 'Marketing'}
```

### Iterating Through Nested Dictionary

You can iterate through a nested dictionary using nested loops to access all key-value pairs:

```python
# Iterating through all employees and their details
for emp_id, emp_info in employees.items():
    print(f"Employee ID: {emp_id}")
    for key, value in emp_info.items():
        print(f"{key}: {value}")
    print()  # Print an empty line for separation
```

### Output:

```
Employee ID: emp1
name: Alice
age: 32
department: HR

Employee ID: emp2
name: Bob
age: 25
department: Engineering

Employee ID: emp3
name: Carol
age: 28
department: Finance

Employee ID: emp4
name: David
age: 35
department: Marketing
```

### Summary

- **Nested Dictionary**: A dictionary that contains other dictionaries as values.
- **Accessing Values**: Use multiple keys to access values at different levels of nesting.
- **Modifying and Adding Entries**: Update values or add new entries using assignment.
- **Iterating Through**: Use nested loops to iterate through all levels of the nested dictionary and access each key-value pair.

Nested dictionaries provide a flexible way to organize and manipulate data structures with multiple levels of hierarchy, making them suitable for handling complex data relationships in Python programs.