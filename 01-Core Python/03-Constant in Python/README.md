# Constant in Python

In Python, there's no strict concept of a "constant" like in some other programming languages where you can declare a variable as constant and its value cannot be changed. However, it's a convention in Python to use uppercase names for variables that are intended to be treated as constants, to indicate to other programmers that the value should not be changed.


### For example:

```python
PI = 3.14159
GRAVITY = 9.8
```

While Python doesn't enforce the immutability of variables declared in this way, it's a widely accepted convention to treat them as constants and not modify their values throughout the program.

If you want to create immutable objects in Python, you can use tuples or frozensets, but note that this applies to the object itself, not the variable name holding a reference to the object.


### For example:

```python
MY_CONSTANT_TUPLE = (1, 2, 3)
MY_CONSTANT_FROZENSET = frozenset([1, 2, 3])
```

Using tuples or frozensets in this way can provide a level of immutability for the values they contain. However, it's important to remember that this doesn't prevent reassignment of the variable name to a different object.