class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} stopped.")

    def honk(self):
        print("Honk!")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2018)

# Accessing attributes
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Accord

# Calling methods
car1.start()  # Output: Toyota Camry started.
car2.honk()   # Output: Honk!

# Accessing and modifying attributes
print(car1.is_running)  # Output: True
car1.stop()  # Output: Toyota Camry stopped.
print(car1.is_running)  # Output: False
