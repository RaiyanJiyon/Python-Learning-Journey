# id Function type Function and getsizeof Function in Python

In Python, the `id`, `type`, and `getsizeof` functions provide useful information about objects. Here’s a detailed look at each of these functions:

### 1. `id` Function

The `id` function returns the unique identifier of an object. This identifier is unique and constant for the object during its lifetime.

#### Syntax

```python
id(object)
```

#### Example

```python
x = 42
print(id(x))  # Output: (an integer unique to the object x)

y = [1, 2, 3]
print(id(y))  # Output: (an integer unique to the object y)
```

The `id` is typically the memory address of the object.

### 2. `type` Function

The `type` function returns the type of an object. It is often used to check the type of an object at runtime.

#### Syntax

```python
type(object)
```

#### Example

```python
a = 10
print(type(a))  # Output: <class 'int'>

b = "Hello"
print(type(b))  # Output: <class 'str'>

c = [1, 2, 3]
print(type(c))  # Output: <class 'list'>
```

### 3. `sys.getsizeof` Function

The `sys.getsizeof` function returns the size of an object in bytes. It includes the overhead of the object.

#### Syntax

```python
import sys
sys.getsizeof(object, default)
```

- **`object`**: The object whose size you want to determine.
- **`default`**: An optional argument that specifies the value to return if the object does not provide size information.

#### Example

```python
import sys

x = 42
print(sys.getsizeof(x))  # Output: (size of integer object in bytes)

y = "Hello, World!"
print(sys.getsizeof(y))  # Output: (size of string object in bytes)

z = [1, 2, 3, 4, 5]
print(sys.getsizeof(z))  # Output: (size of list object in bytes)
```

### Usage in Combination

You can use these functions together to get detailed information about objects:

```python
import sys

data = [1, 2, 3, 4, 5]

print(f"ID: {id(data)}")
print(f"Type: {type(data)}")
print(f"Size: {sys.getsizeof(data)} bytes")

for item in data:
    print(f"Item: {item}, Type: {type(item)}, Size: {sys.getsizeof(item)} bytes")
```

### Summary

- **`id(object)`**: Returns a unique identifier for the object.
- **`type(object)`**: Returns the type of the object.
- **`sys.getsizeof(object)`**: Returns the size of the object in bytes, including overhead.

These functions are invaluable for introspection and debugging, providing insight into the identity, type, and memory usage of objects in Python.