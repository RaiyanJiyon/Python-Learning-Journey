# Class Method in Python


In Python, a class method is a method that is bound to the class rather than the instance of the class. It can be called on both the class itself and its instances. Class methods are defined using the `@classmethod` decorator and have access to the class itself via the first parameter conventionally named cls.

Here's an example demonstrating the use of a class method in Python:

```python
class MyClass:
    class_variable = 10  # Class variable

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

    @classmethod
    def class_method(cls, x):
        print("Class variable:", cls.class_variable)
        print("Called with:", x)

# Calling the class method using the class name
MyClass.class_method(5)
# Output:
# Class variable: 10
# Called with: 5

# Creating an instance of MyClass
obj = MyClass(20)

# Calling the class method using the instance
obj.class_method(7)
# Output:
# Class variable: 10
# Called with: 7
```


In this example, 
- class_method is a class method of the MyClass class. 
- It is defined using the `@classmethod` decorator. 
- Within the method, cls represents the class itself. 
- The class method can access class variables and perform operations related to the class.

You can call a class method using either the class name (`MyClass.class_method(...)`) or an instance of the class (`obj.class_method(...)`). When calling the class method using an instance, Python automatically passes the class of the instance as the first argument (cls)
