# Question 2:
# Print the multiplication table of a number entered by the user
# (1 to 10).

# Step 1: Take the number from the user
number = int(input("Enter a number: "))

# Step 2: Use a for loop to multiply it by 1, 2, 3, ... up to 10
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

# Time Complexity: O(n) -> the loop runs 10 times (a fixed number)
# Space Complexity: O(1) -> only a few variables are stored
