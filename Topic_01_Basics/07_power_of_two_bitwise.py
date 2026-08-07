# Question 7:
# Given a number n, use bitwise operators to check if n is a power of 2
# (n & (n-1) == 0).

n = int(input("Enter a positive integer: "))

# A power of 2 has exactly one bit set (e.g. 8 = 1000).
# Subtracting 1 flips all bits after that single set bit
# (e.g. 7 = 0111), so ANDing the two gives 0 only for powers of 2.
# n must also be > 0, since 0 & -1 would otherwise falsely pass.
is_power_of_two = n > 0 and (n & (n - 1)) == 0

if is_power_of_two:
    print(f"{n} is a power of 2")
else:
    print(f"{n} is NOT a power of 2")

# Time Complexity: O(1)
# Space Complexity: O(1)
