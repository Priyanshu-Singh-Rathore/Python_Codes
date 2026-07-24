# Question 5:
# Take the radius of a circle as input and print its area and
# circumference (use 3.14159 for pi).

PI = 3.14159

radius = float(input("Enter the radius of the circle: "))
area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Time Complexity: O(1) 
# Space Complexity: O(1)
