# This program will calculate the area and perimeter of a rectangle

# Ask the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Print out the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
