# Question 4:
# Check whether a number is prime using a loop, then print all prime
# numbers between 1 and 100.

# Part 1: Check if one number entered by the user is prime
number = int(input("Enter a number: "))

is_prime = True

if number < 2:
    is_prime = False
else:
    # Check if any number from 2 to (number - 1) divides it evenly
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i = i + 1

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# Part 2: Print all prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for current in range(2, 101):
    is_prime = True
    i = 2
    while i < current:
        if current % i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime:
        print(current)

# Time Complexity: O(n) for checking one number (we loop up to n).
#                  For printing all primes up to 100, it is O(n^2)
#                  in the worst case, since we check every number
#                  from 2 to 100 and each check can loop up to that
#                  number.
# Space Complexity: O(1) -> only a few variables are stored
