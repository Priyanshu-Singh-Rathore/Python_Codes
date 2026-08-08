# Question 10:
# Write a number-guessing game: the program picks a random number
# between 1 and 100, and the user keeps guessing (via a loop) until
# they get it right, with "too high"/"too low" hints after each guess.

import random

# Step 1: Let the computer pick a random secret number
secret_number = random.randint(1, 100)

# Step 2: Keep count of how many guesses the user has made
number_of_guesses = 0

print("I am thinking of a number between 1 and 100. Try to guess it!")

# Step 3: Keep looping until the user guesses correctly
guessed_correctly = False
while guessed_correctly == False:
    guess = int(input("Enter your guess: "))
    number_of_guesses = number_of_guesses + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it in", number_of_guesses, "tries.")
        guessed_correctly = True

# Time Complexity: O(1) per guess check. The total number of loop runs
#                  depends on how many guesses the user needs, which
#                  is not fixed, so we cannot give one exact number.
# Space Complexity: O(1) -> only a few variables are stored
