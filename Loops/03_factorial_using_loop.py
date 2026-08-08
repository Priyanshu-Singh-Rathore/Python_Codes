# Question 3:
# Calculate the factorial of a number using a loop (not recursion).

# Step 1: Take the number from the user
number = int(input("Enter a number: "))

# Step 2: Start with factorial = 1, then multiply it by every number
# from 1 up to the given number
factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i = i + 1

# Step 3: Print the final result
print("Factorial of", number, "is", factorial)

# Time Complexity: O(n) -> the loop runs 'number' times
# Space Complexity: O(1) -> only a few variables are stored
