# Question 8:
# Find the sum of digits of a number, and repeat the process until the
# result is a single digit (digital root), using a loop.

number = int(input("Enter a number: "))
while number >= 10:
    digit_sum = 0
    while number > 0:
        last_digit = number % 10
        digit_sum = digit_sum + last_digit
        number = number // 10
    number = digit_sum

print("The digital root is:", number)

# Time Complexity: O(n)
# Space Complexity: O(1)
