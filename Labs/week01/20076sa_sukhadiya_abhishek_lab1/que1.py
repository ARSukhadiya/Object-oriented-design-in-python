import random

# The program title
print("Guess a random number")

# Generate a random number between 1 and 100
number = random.randint(1, 100)
print("Random number (between 1 and 100) has been generated.")
num_of_guess = 0

# Ask the user to guess the number repeatedly until the guess is correct
while True:
    guess = int(input("Please guess a number between 1 and 100:"))
    num_of_guess += 1 

    if guess < number:
        print("Too Low! Try again.")
    elif guess > number:
        print("Too High! Try again.")
    else:
        print("Congratulations! Your guess is correct. You tried", num_of_guess, "times")
        break
