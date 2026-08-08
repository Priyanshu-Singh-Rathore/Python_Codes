# Question 1:
# Print all numbers from 1 to 50 using a for loop, and all numbers
# from 50 to 1 using a while loop.

# Part 1: Using a for loop to count up from 1 to 50
print("Counting up with a for loop:")
for number in range(1, 51):
    print(number)

# Part 2: Using a while loop to count down from 50 to 1
print("Counting down with a while loop:")
number = 50
while number >= 1:
    print(number)
    number = number - 1

# Time Complexity: O(n)
# Space Complexity: O(1)
