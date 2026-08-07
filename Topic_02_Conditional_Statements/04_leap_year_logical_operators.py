# Question 4:
# Write a program that checks whether a year is a leap year using
# logical operators (and, or).

year = int(input("Enter a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Time Complexity: O(1)
# Space Complexity: O(1)
