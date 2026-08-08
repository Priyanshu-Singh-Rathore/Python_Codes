# Question 7:
# Print the following pattern for n rows using nested loops:
# *
# * *
# * * *
# * * * *

# Step 1: Take the number of rows from the user
n = int(input("Enter number of rows: "))

# Step 2: The outer loop moves down row by row
for row in range(1, n + 1):
    line = ""
    # Step 3: The inner loop adds one star for each column in this row
    for column in range(1, row + 1):
        line = line + "* "
    # Step 4: Print the finished line for this row
    print(line)

# Time Complexity: O(n^2) -> the inner loop runs more times as the
#                  outer loop grows, giving a total of about n*(n+1)/2
#                  star prints
# Space Complexity: O(n) -> the longest line stores up to n stars
