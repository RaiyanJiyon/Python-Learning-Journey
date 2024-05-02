class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def bark(self):
        print(f"{self.name} barks")

# Creating an instance of Dog
dog = Dog("Buddy")

# Accessing attributes and methods
print(dog.species)  # Output: Dog
dog.speak()         # Output: Animal speaks
dog.bark()          # Output: Buddy barks