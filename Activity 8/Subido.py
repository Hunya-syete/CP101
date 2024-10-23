import random

# 1. Generate a random number between 1 and 20.
secret_number = random.randint(1, 20)

# 4. Allow the user to keep guessing until they reach a maximum of 3 attempts.
attempts_remaining = 3

# 5. Use a loop for the guessing process.
while attempts_remaining > 0:
    print(f"\nYou have {attempts_remaining} attempts left.")

    # 2. Allow the user to guess the number.
    try:
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Go back to the beginning of the loop

    # 3. Provide feedback on whether the guess is correct, too high, or too low.
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break  # Exit the loop if the guess is correct
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts_remaining -= 1  # Decrement the number of attempts

# Message if the user runs out of attempts
if attempts_remaining == 0:
    print(f"\nYou ran out of attempts. The number was {secret_number}.")
