# Question 3:
# Calculate the factorial of a number using a loop (not recursion).


number = int(input("Enter a number: "))

factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i = i + 1


print("Factorial of", number, "is", factorial)

# Time Complexity: O(n)
# Space Complexity: O(1)
