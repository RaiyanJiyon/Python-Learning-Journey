x = 42
y = 42
print(id(x))  # Output: Memory address of x
print(id(y))  # Output: Memory address of y (same as x)

x = 42
print(type(x))  # Output: <class 'int'>


import sys
x = [1, 2, 3]
print(sys.getsizeof(x))  # Output: Size of the list object in bytes