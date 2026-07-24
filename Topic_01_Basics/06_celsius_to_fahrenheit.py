# Question 6:
# Take a temperature in Celsius as input and convert it to Fahrenheit,
# printing the result.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# Time Complexity: O(1) 
# Space Complexity: O(1)
