# Operator overloading in Python

Operator overloading in Python refers to the ability to define how operators such as +, -, *, /, ==, !=, etc., behave for user-defined classes. By overloading operators, you can customize their behavior to work with objects of your own classes.

In Python, operator overloading is achieved by defining special methods with predefined names that Python recognizes and calls when certain operators are used with objects of your class. These special methods are also called "magic" or "dunder" (double underscore) methods.

Here are some commonly used special methods for operator overloading:

- `__add__(self, other)`: Defines behavior for the + operator.
- `__sub__(self, other)`: Defines behavior for the - operator.
- `__mul__(self, other)`: Defines behavior for the * operator.
- `__truediv__(self, other)`: Defines behavior for the / operator.
- `__eq__(self, other)`: Defines behavior for the == operator.
- `__ne__(self, other)`: Defines behavior for the != operator.
- `__lt__(self, other)`: Defines behavior for the < operator.
- `__le__(self, other)`: Defines behavior for the <= operator.
- `__gt__(self, other)`: Defines behavior for the > operator.
- `__ge__(self, other)`: Defines behavior for the >= operator.
- `__getitem__(self, key)`: Defines behavior for indexing, using square brackets [].
- `__setitem__(self, key, value)`: Defines behavior for assigning to an indexed item.
- `__len__(self)`: Defines behavior for the len() function.
