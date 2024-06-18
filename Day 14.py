# Define a class called "Rectangle"
class Rectangle:
    def __init__(self, width, height):
        # Initialize the attributes of the Rectangle class
        self.width = width
        self.height = height

    def area(self):
        # Method to calculate the area of the rectangle
        return self.width * self.height

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle
        return 2 * (self.width + self.height)

# Create an instance of the Rectangle class
my_rectangle = Rectangle(5, 10)

# Calculate the area of the rectangle
print(f"Area: {my_rectangle.area()}")

# Calculate the perimeter of the rectangle
print(f"Perimeter: {my_rectangle.perimeter()}")
