'''
In Python, a constructor is a special method called __init__() that gets invoked automatically when an object of a class is created. It's used to initialize the object's attributes.

Here's an example demonstrating the use of a constructor in a Python class:
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and calling methods
person1.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.
person2.introduce()  # Output: Hi, I'm Bob and I'm 25 years old.

# Accessing attributes directly
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25


'''
In this example, the __init__() method serves as the constructor. It takes two parameters, name and age, and initializes the name and age attributes of the objects created from the Person class.

When person1 and person2 objects are created, the __init__() method is automatically called with the arguments provided, and the attributes name and age are set accordingly. This allows us to create objects with initial states defined by the constructor.
'''