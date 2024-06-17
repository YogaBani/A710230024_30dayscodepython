# Define a class called "Car"
class Car:
    def __init__(self, brand, model, year):
        # Initialize the attributes of the Car class
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        # Method to drive the car and update the mileage
        self.mileage += miles

    def describe_car(self):
        # Method to describe the car
        print(f"This car is a {self.year} {self.brand} {self.model} with {self.mileage} miles.")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2015)

# Drive the car
my_car.drive(100)

# Describe the car
my_car.describe_car()
