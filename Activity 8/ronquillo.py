import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)  # Generates a random number between 1 and 20
    attempts = 3  # User has 3 attempts

    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess the correct number.")

    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}/{attempts} - Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempt + 1} attempts.")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()
Welcome to 'Guess the Number' game!

I have selected a number between 1 and 20.

You have 3 attempts to guess the correct number.

Attempt 1/3 - Enter your guess: 8

Too low! Try again.

Attempt 2/3 - Enter your guess: 9

Congratulations! You guessed the number 9 correctly in 2 attempts.



=== Code Execution Successful ===
