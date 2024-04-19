'''
In Python, you can call the constructor of the parent class from the constructor of the child class using the super() function. This allows you to reuse the initialization logic defined in the parent class and extend it as needed in the child class.

Here's an example demonstrating how to call the parent class constructor in a child class using the super() function:
'''

class Parent:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
        print("Parent constructor")

class Child(Parent):
    def __init__(self, parent_attr, child_attr):
        # Call parent class constructor
        super().__init__(parent_attr)
        self.child_attr = child_attr
        print("Child constructor")

# Creating an instance of Child
child = Child("Parent value", "Child value")

# Accessing attributes
print(child.parent_attr)  # Output: Parent value
print(child.child_attr)   # Output: Child value
