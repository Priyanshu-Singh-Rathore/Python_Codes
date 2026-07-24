# Question 7:
# Write a program that asks for a person's age and prints how many days
# old they are (approximate, ignore leap years).

DAYS_PER_YEAR = 365

age = int(input("Enter your age in years: "))
days_old = age * DAYS_PER_YEAR

print(f"You are approximately {days_old} days old.")

# Time Complexity: O(1) 
# Space Complexity: O(1)

