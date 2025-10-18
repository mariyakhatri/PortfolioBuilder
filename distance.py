import math

# Function to find distance between two points
def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Call the function
result = find_distance(x1, y1, x2, y2)

# Display the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {result:.2f}")
