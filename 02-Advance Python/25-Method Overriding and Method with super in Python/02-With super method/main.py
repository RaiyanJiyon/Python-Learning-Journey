'''
Now, let's discuss the super() function. In Python, the super() function is used to call methods and access attributes of the superclass from within a subclass. It allows you to invoke the superclass's methods and constructors explicitly, enabling cooperative inheritance and avoiding redundancy.

Here's an example demonstrating the use of super() to call the superclass method from within the subclass:
'''


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


'''
In this example:

The Dog class overrides the speak() method defined in its superclass, Animal.
Inside the speak() method of Dog, super().speak() is used to call the speak() method of the superclass Animal.
As a result, both "Animal speaks" and "Dog barks" are printed when calling the speak() method on an instance of Dog.
'''