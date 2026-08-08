# Question 9:
# Use break and continue to print all numbers from 1 to 100 that are
# NOT divisible by 3 or 5, and stop the loop entirely once you've
# printed 20 such numbers.

# Step 1: Keep count of how many numbers we have printed so far
count_printed = 0

# Step 2: Go through numbers from 1 to 100
for number in range(1, 101):

    # Step 3: If the number IS divisible by 3 or 5, skip it
    if number % 3 == 0 or number % 5 == 0:
        continue

    # Step 4: Otherwise print it and count it
    print(number)
    count_printed = count_printed + 1

    # Step 5: Stop completely once we have printed 20 numbers
    if count_printed == 20:
        break

# Time Complexity: O(n) -> in the worst case we check up to 100 numbers
# Space Complexity: O(1) -> only a few variables are stored
