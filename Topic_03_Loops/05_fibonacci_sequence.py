# Question 5:
# Print the Fibonacci sequence up to n terms using a loop.

n = int(input("Enter number of terms: "))
first = 0
second = 1

print("Fibonacci sequence:")

count = 0
while count < n:
    print(first)
    next_number = first + second
    first = second
    second = next_number
    count = count + 1

# Time Complexity: O(n)
# Space Complexity: O(1)
