class Animal:
    def move(self):
        pass

class Vehicle:
    def move(self):
        pass

# Animal subclasses
class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

# Vehicle subclasses
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Demonstration function
def demonstrate_movement(objects):
    for obj in objects:
        print(f"{obj.__class__.__name__}: {obj.move()}")

# Create instances
animals = [Dog(), Fish(), Bird()]
vehicles = [Car(), Bicycle(), Plane(), Boat()]

print("Animals in motion:")
demonstrate_movement(animals)

print("\nVehicles in motion:")
demonstrate_movement(vehicles)