# Question 10:
# Given two boolean values from user input, print the result of AND, OR,
# NOT, and XOR (!= can simulate XOR for booleans) operations on them.

val1 = input("Enter first boolean (True/False): ").strip().lower() == "true"
val2 = input("Enter second boolean (True/False): ").strip().lower() == "true"

print(f"val1 = {val1}, val2 = {val2}")
print(f"AND: {val1 and val2}")
print(f"OR: {val1 or val2}")
print(f"NOT val1: {not val1}")
print(f"NOT val2: {not val2}")
print(f"XOR: {val1 != val2}")  # True only when exactly one is True

# Time Complexity: O(1)
# Space Complexity: O(1)
