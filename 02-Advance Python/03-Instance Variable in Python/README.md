# Instance Variable in Python

In Python, instance variables are variables that belong to a specific instance of a class. Each object (instance) of the class can have its own instance variables. These variables are defined within methods of the class using the self keyword.

Here's an example to illustrate instance variables:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = None  # Initially grade is set to None

    def set_grade(self, grade):
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Creating objects (instances) of the Student class
student1 = Student("Raiyan", 20)
student2 = Student("Sabbir", 22)

# Accessing and modifying instance variables
student1.set_grade("A")
student2.set_grade("B+")

# Displaying information
student1.display_info()
student2.display_info()
```


In this example, 
- name, age, and grade are instance variables of the Student class. 
- They are accessed and modified using the self keyword within the methods of the class.

When objects student1 and student2 are created, each instance gets its own copy of name, age, and grade. These variables are unique to each instance, and changes made to them affect only the specific instance they belong to.
