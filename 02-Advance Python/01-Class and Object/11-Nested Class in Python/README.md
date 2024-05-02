# Nested Class in Python

In Python, a nested class is a class defined within another class. Nested classes are sometimes referred to as inner classes. They are useful when a class is only relevant to its containing class or when you want to logically group classes together.

Here's an example demonstrating the use of a nested class in Python:

```python
class OuterClass:
    def __init__(self, outer_attr):
        self.outer_attr = outer_attr

    class InnerClass:
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr

        def display(self):
            print(f"Inner attribute: {self.inner_attr}")

# Creating an instance of the outer class
outer_obj = OuterClass("outer_value")

# Creating an instance of the inner class using the outer class
inner_obj = outer_obj.InnerClass("inner_value")

# Accessing and calling methods of the inner class
inner_obj.display()  # Output: Inner attribute: inner_value
```


In this example, 
- InnerClass is defined within OuterClass. 
- InnerClass has access to the attributes and methods of OuterClass, but the reverse is not true. 
- InnerClass is instantiated using an instance of OuterClass.

Nested classes can be useful for organizing related classes together, especially when the inner class is tightly coupled with the outer class and doesn't make sense to be used independently. They can also help in reducing namespace pollution by encapsulating implementation details within the outer class. However, nested classes should be used judiciously, as they can increase the complexity of the code and reduce readability if overused.
