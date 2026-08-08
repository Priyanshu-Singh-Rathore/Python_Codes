# Question 2:
# Print the multiplication table of a number entered by the user
# (1 to 10).


number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

# Time Complexity: O(n)
# Space Complexity: O(1)
