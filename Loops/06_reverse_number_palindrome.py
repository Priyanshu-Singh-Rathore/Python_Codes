# Question 6:
# Reverse a number using a loop (e.g. 1234 -> 4321) and check if it's
# a palindrome.


number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10

print("Reversed number:", reversed_number)
if original_number == reversed_number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

# Time Complexity: O(d)
# Space Complexity: O(1)
