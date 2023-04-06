import random

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

secret_number = random.randint(1, 100)
num_guesses = 0

while True:
    guess = input("Enter your guess (or 'q' to quit): ")

    if guess == 'q':
        print("Thanks for playing!")
        break

    num_guesses += 1
    guess = int(guess)

    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses!")
        break
    elif guess < secret_number:
        print("Too low! Guess higher.")
    else:
        print("Too high! Guess lower.")