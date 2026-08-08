# Question 6:
# Reverse a number using a loop (e.g. 1234 -> 4321) and check if it's
# a palindrome.

# Step 1: Take the number from the user
number = int(input("Enter a number: "))

# Step 2: Keep the original number safe for comparison later
original_number = number

# Step 3: Build the reversed number one digit at a time
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10

print("Reversed number:", reversed_number)

# Step 4: Compare the reversed number with the original number
if original_number == reversed_number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

# Time Complexity: O(d) -> where d is the number of digits in the number
# Space Complexity: O(1) -> only a few variables are stored
