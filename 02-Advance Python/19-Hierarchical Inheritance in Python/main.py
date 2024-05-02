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

class Cat(Animal):  
    def __init__(self, name, color):
        super().__init__("Cat")
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} meows")

# Creating instances of Dog and Cat
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "White")

# Accessing attributes and methods
print(dog.species)  # Output: Dog
print(dog.name)     # Output: Buddy
print(dog.breed)    # Output: Labrador
dog.speak()         # Output: Animal speaks
dog.bark()          # Output: Buddy barks

print(cat.species)  # Output: Cat
print(cat.name)     # Output: Whiskers
print(cat.color)    # Output: White
cat.speak()         # Output: Animal speaks
cat.meow()          # Output: Whiskers meows