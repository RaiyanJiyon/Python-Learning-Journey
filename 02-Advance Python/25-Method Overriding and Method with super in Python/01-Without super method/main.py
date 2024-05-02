class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def speak(self):
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()

# Calling the speak method
dog.speak()  # Output: Dog barks