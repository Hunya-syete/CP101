import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
max_attempts = 3

your_name = input("What is your name?: ")
print(f"Hello {your_name}, Welcome to guess the number! 🙂 ")
print("Guess a number from 1 to 20")

# Loop through the attempts
for attempt in range(1, max_attempts + 1):
    # Get the user's guess
    guess = int(input(f"You have {attempt}/{max_attempts} attempts,  kindly enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low bruh.")
    else:
        print("Too high bruh")

    # Check if this was the last attempt
    if attempt == max_attempts:
        print(f"Sorry, naubos na iyong free trial. The correct number was {secret_number}.")
