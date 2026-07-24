# Question 4:
# Swap the values of two variables a and b without using a third variable.

a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Python's tuple packing/unpacking swaps values in a single line,
# with no temporary variable needed.
a, b = b, a

print(f"After swap: a = {a}, b = {b}")

# Time Complexity: O(1)
# Space Complexity: O(1)
