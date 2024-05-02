class Student:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    # Accessor method (getter)
    def get_name(self):
        return self._name

    # Accessor method (getter)
    def get_age(self):
        return self._age

    # Mutator method (setter)
    def set_name(self, name):
        self._name = name

    # Mutator method (setter)
    def set_age(self, age):
        if age >= 0:  # Ensuring age is non-negative
            self._age = age
        else:
            print("Age cannot be negative.")

# Creating an object (instance) of the Student class
student1 = Student("Raiyan", 20)

# Using accessor methods to retrieve attribute values
print("Name:", student1.get_name())  # Output: Name: Raiyan
print("Age:", student1.get_age())    # Output: Age: 20

# Using mutator methods to update attribute values
student1.set_name("Jiyon")
student1.set_age(22)
print("Updated name:", student1.get_name())  # Output: Updated name: Jiyon
print("Updated age:", student1.get_age())    # Output: Updated age: 22

# Trying to set negative age
student1.set_age(-5)  # Output: Age cannot be negative.
print("Age after invalid update:", student1.get_age())  # Output: Age after invalid update: 22