# Multiple Inheritance and Method Resolution Order in Python

Multiple inheritance in Python refers to a scenario where a class can inherit attributes and methods from more than one parent class. This allows for the creation of complex class hierarchies where a subclass inherits from multiple superclasses.

When dealing with multiple inheritance, Python uses a method resolution order (MRO) to determine the order in which methods should be called. The MRO defines the sequence in which base classes are searched when looking for a method or attribute.

Here's an example demonstrating multiple inheritance and method resolution order in Python:

```python
class A:
    def method(self):
        print("Method of class A")

class B:
    def method(self):
        print("Method of class B")

class C(A, B):  # Multiple inheritance
    pass

class D(B, A):  # Another example of multiple inheritance
    pass

# Creating instances of C and D
c = C()
d = D()

# Calling the method
c.method()  # Output: Method of class A
d.method()  # Output: Method of class B
```

In this example:

- Class C and class D both inherit from classes A and B, resulting in multiple inheritance.
- When calling the method() of instances c and d, Python uses the MRO to determine the order in which to search for the method:
- For c, the method is found in class A, so it prints "Method of class A".
- For d, the method is found in class B, so it prints "Method of class B".
- Python uses the C3 linearization algorithm to compute the MRO, which ensures a consistent and predictable method resolution order. 
- This algorithm takes into account the order in which base classes are specified in the subclass definition, as well as any conflicts or diamond inheritance patterns that may arise.

Understanding method resolution order is important when working with multiple inheritance in Python, as it determines the behavior of method and attribute lookup in subclasses.