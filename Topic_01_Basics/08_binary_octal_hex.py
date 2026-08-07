# Question 8:
# Write a program that takes a number and prints its binary, octal, and
# hexadecimal representations using bitwise/format tricks or built-in
# functions.

num = int(input("Enter a number: "))

# Using built-in functions (bin, oct, hex):
print(f"Binary: {bin(num)}")
print(f"Octal: {oct(num)}")
print(f"Hexadecimal: {hex(num)}")

print(f"Binary (format): {format(num, 'b')}")
print(f"Octal (format): {format(num, 'o')}")
print(f"Hexadecimal (format): {format(num, 'x')}")

# Time Complexity: O(log n)
# Space Complexity: O(log n)
