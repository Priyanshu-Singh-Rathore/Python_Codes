# Question 8:
# Find the sum of digits of a number, and repeat the process until the
# result is a single digit (digital root), using a loop.

# Step 1: Take the number from the user
number = int(input("Enter a number: "))

# Step 2: Keep adding digits together until only one digit is left
while number >= 10:
    digit_sum = 0
    # Step 3: Add up all the digits of the current number
    while number > 0:
        last_digit = number % 10
        digit_sum = digit_sum + last_digit
        number = number // 10
    # Step 4: The digit sum becomes the new number to check
    number = digit_sum

print("The digital root is:", number)

# Time Complexity: O(d) -> where d is the number of digits, since the
#                  digit sum shrinks the number quickly with each pass
# Space Complexity: O(1) -> only a few variables are stored
