# Question 9:
# Take marks out of 100 and use chained comparison operators
# (e.g. 90 <= marks <= 100) to assign a grade (A/B/C/D/F).

marks = float(input("Enter marks (out of 100): "))

if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks < 90:
    grade = "B"
elif 60 <= marks < 75:
    grade = "C"
elif 40 <= marks < 60:
    grade = "D"
elif 0 <= marks < 40:
    grade = "F"
else:
    grade = "Invalid marks"

print(f"Grade: {grade}")

# Time Complexity: O(1)
# Space Complexity: O(1)
