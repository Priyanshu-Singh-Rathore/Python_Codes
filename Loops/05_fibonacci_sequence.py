# Question 5:
# Print the Fibonacci sequence up to n terms using a loop.

# Step 1: Take the number of terms from the user
n = int(input("Enter number of terms: "))

# Step 2: The first two Fibonacci numbers are 0 and 1
first = 0
second = 1

print("Fibonacci sequence:")

count = 0
while count < n:
    print(first)
    # Step 3: Calculate the next number by adding the last two
    next_number = first + second
    # Step 4: Move both numbers forward by one step
    first = second
    second = next_number
    count = count + 1

# Time Complexity: O(n) -> the loop runs exactly n times
# Space Complexity: O(1) -> only a few variables are stored
