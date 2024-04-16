'''
In Python, you can pass an instance of one class as an argument to a method of another class just like passing any other object. This allows for interaction between different classes and facilitates code reusability and modularity.

Here's an example demonstrating how to pass an instance of one class to a method of another class:
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student:
    def __init__(self, person):
        self.person = person

    def display_person_info(self):
        print("Person Information:")
        self.person.display_info()

# Creating an instance of Person
person = Person("Jiyon", 25)

# Creating an instance of Student and passing the Person instance as an argument
student = Student(person)

# Calling the method of Student class to display person information
student.display_person_info()


'''
In this example, we have two classes: Person and Student. The Person class defines a person with attributes name and age, as well as a method display_info() to display the person's information. The Student class takes an instance of the Person class as an argument to its constructor and stores it as an attribute person. It also has a method display_person_info() to display the information of the person stored in the person attribute.

By passing an instance of the Person class to the Student class, we allow the Student class to interact with the attributes and methods of the Person class. This promotes code reusability and modularity by separating concerns and allowing classes to collaborate with each other.
'''