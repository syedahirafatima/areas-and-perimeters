import math
# input data from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate area
area = (base * height) / 2

# Calculate perimeter
perimeter = side1 + side2 + side3

# Display results
print("The area of the triangle is:", area)
print("The perimeter of the triangle is:", perimeter)
