# f String or Formatted String Literal in Python

Formatted string literals, also known as f-strings, were introduced in Python 3.6. They provide a concise and readable way to embed expressions inside string literals using curly braces `{}`. F-strings are prefixed with an `f` or `F` before the opening quotation mark.

### Syntax

The basic syntax for an f-string is:

```python
f"string {expression}"
```

- **`f`**: Prefix that indicates an f-string.
- **`"string"`**: The string that contains expressions to be evaluated and embedded.
- **`{expression}`**: An expression whose result will be embedded in the string.

### Examples

#### Example 1: Basic Usage

```python
name = "Alice"
age = 30

formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."
```

#### Example 2: Inline Expressions

You can include arbitrary expressions inside f-strings:

```python
width = 5
height = 10

area = f"The area of the rectangle is {width * height} square units."
print(area)  # Output: "The area of the rectangle is 50 square units."
```

#### Example 3: Calling Functions

You can call functions inside f-strings:

```python
def greet(name):
    return f"Hello, {name}!"

formatted_string = f"{greet('Bob')}, welcome to the party."
print(formatted_string)  # Output: "Hello, Bob!, welcome to the party."
```

### Advanced Formatting

#### Example 4: Formatting Numbers

You can format numbers directly within f-strings:

```python
pi = 3.141592653589793

formatted_string = f"Pi to three decimal places: {pi:.3f}"
print(formatted_string)  # Output: "Pi to three decimal places: 3.142"
```

#### Example 5: Padding and Alignment

You can align text and numbers within f-strings:

```python
name = "Alice"

# Right-align with padding
formatted_string = f"Name: {name:>10}"
print(formatted_string)  # Output: "Name:      Alice"

# Left-align with padding
formatted_string = f"Name: {name:<10}"
print(formatted_string)  # Output: "Name: Alice     "

# Center-align with padding
formatted_string = f"Name: {name:^10}"
print(formatted_string)  # Output: "Name:   Alice   "
```

### Using Dictionaries

You can use dictionaries inside f-strings:

```python
data = {'name': 'Charlie', 'age': 28}

formatted_string = f"Name: {data['name']}, Age: {data['age']}"
print(formatted_string)  # Output: "Name: Charlie, Age: 28"
```

### Using Objects

You can access attributes of objects within f-strings:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("David", 35)

formatted_string = f"Name: {person.name}, Age: {person.age}"
print(formatted_string)  # Output: "Name: David, Age: 35"
```

### f-Strings with `=`

Starting from Python 3.8, you can use the `=` specifier to include both the expression and its result in the output, which is useful for debugging:

```python
value = 42

formatted_string = f"value = {value}"
print(formatted_string)  # Output: "value = 42"
```

### Conclusion

F-strings in Python provide a powerful, readable, and concise way to format strings by embedding expressions directly within string literals. They are preferable to older formatting methods due to their readability and efficiency, making them a great choice for modern Python code.