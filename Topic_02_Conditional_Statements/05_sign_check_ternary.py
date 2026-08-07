# Question 5:
# Take a number and print whether it is positive, negative, or zero
# using a single expression with conditional (ternary) operator syntax.

num = float(input("Enter a number: "))

result = "positive" if num > 0 else ("negative" if num < 0 else "zero")
print(f"The number is {result}")

# Time Complexity: O(1)
# Space Complexity: O(1)
