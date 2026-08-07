# Question 7:
# Given a number n, use bitwise operators to check if n is a power of 2
# (n & (n-1) == 0).

n = int(input("Enter a positive integer: "))

is_power_of_two = n > 0 and (n & (n - 1)) == 0

if is_power_of_two:
    print(f"{n} is a power of 2")
else:
    print(f"{n} is NOT a power of 2")

# Time Complexity: O(1)
# Space Complexity: O(1)
