# Access Nested Dictionary using for Loop in Python

Accessing nested dictionaries using a `for` loop in Python involves iterating through each level of the dictionary hierarchy. Here's how you can access and print values from nested dictionaries using `for` loops:

### Example: Nested Dictionary Access

Consider a nested dictionary representing employee details:

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

#### Accessing Nested Dictionary Using `for` Loops

1. **Iterate over Keys of Outer Dictionary**:
   - Use the `items()` method to iterate over key-value pairs of the outer dictionary.

2. **Access Inner Dictionary**:
   - Within the loop, access each inner dictionary using its key.

3. **Iterate over Keys of Inner Dictionary**:
   - Use another `for` loop to iterate over key-value pairs of each inner dictionary.

4. **Print or Manipulate Values**:
   - Access and print specific values or perform operations as needed.

### Example Code

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

# Iterate over each employee
for emp_id, emp_info in employees.items():
    print(f"Employee ID: {emp_id}")
    
    # Iterate over each key-value pair in the inner dictionary
    for key, value in emp_info.items():
        print(f"{key}: {value}")
    
    print()  # Print an empty line for separation
```

### Output

```
Employee ID: emp1
name: Alice
age: 30
department: HR

Employee ID: emp2
name: Bob
age: 25
department: IT

Employee ID: emp3
name: Carol
age: 28
department: Finance
```

### Explanation

- **Outer Loop (`for emp_id, emp_info in employees.items()`)**:
  - Iterates over each employee (`emp1`, `emp2`, `emp3`) in the `employees` dictionary.
  - `emp_id` represents the employee ID (`'emp1'`, `'emp2'`, `'emp3'`).
  - `emp_info` represents the inner dictionary for each employee (`{'name': 'Alice', 'age': 30, 'department': 'HR'}`, etc.).

- **Inner Loop (`for key, value in emp_info.items()`)**:
  - Iterates over each key-value pair (`'name': 'Alice'`, `'age': 30`, `'department': 'HR'`) in `emp_info`.
  - `key` represents the key (`'name'`, `'age'`, `'department'`).
  - `value` represents the corresponding value (`'Alice'`, `30`, `'HR'`).

- **Printing**:
  - Values are printed in a structured format for each employee and each key-value pair within their details.

### Summary

Using nested `for` loops is effective for accessing and processing data within nested dictionaries. It allows you to navigate through hierarchical data structures and perform operations on specific elements at different levels of nesting.