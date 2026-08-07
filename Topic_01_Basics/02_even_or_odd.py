# Question 2:
# Write a program to check if a given number is even or odd using the
# modulus operator.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Time Complexity: O(1)
# Space Complexity: O(1)
