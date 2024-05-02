class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")

class Labrador(Dog):  
    def __init__(self, name):
        super().__init__(name, "Labrador")

# Creating an instance of Labrador
labrador = Labrador("Buddy")

# Accessing attributes and methods
print(labrador.species)  # Output: Dog
print(labrador.name)     # Output: Buddy
print(labrador.breed)    # Output: Labrador
labrador.speak()         # Output: Animal speaks
labrador.bark()          # Output: Buddy barks