#So this will get input from user
length = float(input("Enter the length of the rectangle in cm: "))
width = float(input("Enter the width of the rectangle in cm: "))

# Calculate area
area = length * width

# Calculate perimeter
perimeter = 2 * (length + width)

# Presenting the results
print("The area of the rectangle is:",  area,"cm²")
print("The perimeter of the rectangle is:", perimeter,"cm")
