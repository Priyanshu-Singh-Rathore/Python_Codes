# Question 9:
# Use break and continue to print all numbers from 1 to 100 that are
# NOT divisible by 3 or 5, and stop the loop entirely once you've
# printed 20 such numbers.

count_printed = 0

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        continue
    print(number)
    count_printed = count_printed + 1
    if count_printed == 20:
        break

# Time Complexity: O(n)
# Space Complexity: O(1)
