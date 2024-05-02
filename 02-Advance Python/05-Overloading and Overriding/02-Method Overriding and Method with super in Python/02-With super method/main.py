class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def speak(self):
        super().speak()  # Call the speak() method of the superclass
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()

# Calling the speak method
dog.speak()  