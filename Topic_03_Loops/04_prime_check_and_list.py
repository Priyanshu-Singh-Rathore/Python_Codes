# Question 4:
# Check whether a number is prime using a loop, then print all prime
# numbers between 1 and 100.

number = int(input("Enter a number: "))
is_prime = True
if number < 2:
    is_prime = False
else:
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

# Time Complexity: O(n)
# Space Complexity: O(1)
