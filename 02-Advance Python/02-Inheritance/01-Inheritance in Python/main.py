class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks")

# Creating instances of the classes
animal = Animal("Cat")
dog = Dog("Buddy")

# Calling methods
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Buddy barks