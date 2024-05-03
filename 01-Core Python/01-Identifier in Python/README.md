# Identifier in Python

In Python, an identifier is a name used to identify a variable, function, class, module, or other object. Identifiers must follow certain rules:

1. They can contain letters (both uppercase and lowercase), digits, and underscores.
2. They must start with a letter `(a-z, A-Z)` or an underscore `(_)`.
3. They cannot start with a digit `(0-9)`.
4. Python `keywords` cannot be used as identifiers.

## Here are some examples of valid identifiers:

```python
my_variable = 10
my_function = lambda x: x**2
# MyClass = MyClass()
_underscore_variable = 42
```

## Here are examples of invalid identifiers:

```python
2variable = 10  # Starts with a digit
for = 5         # Uses a Python keyword as an identifier
my-variable = 3 # Contains a hyphen
```