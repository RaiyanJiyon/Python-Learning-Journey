class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Calling instance methods
dog1.bark()  # Output: Buddy says: Woof!
dog2.bark()  # Output: Max says: Woof!

# Accessing and modifying attributes through instance methods
dog1.celebrate_birthday()  # Output: Buddy is now 4 years old!
dog2.celebrate_birthday()  # Output: Max is now 6 years old!