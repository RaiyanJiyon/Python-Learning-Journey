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
