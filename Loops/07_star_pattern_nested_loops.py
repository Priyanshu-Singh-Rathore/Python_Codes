# Question 7:
# Print the following pattern for n rows using nested loops:
# *
# * *
# * * *
# * * * *

n = int(input("Enter number of rows: "))

for row in range(1, n + 1):
    line = ""
    for column in range(1, row + 1):
        line = line + "* "
    print(line)

# Time Complexity: O(n^2)
# Space Complexity: O(n)
