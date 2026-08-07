# Question 3:
# Given three numbers, find the largest using only comparison operators
# (no built-in max()).

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")

# Time Complexity: O(1)
# Space Complexity: O(1)
