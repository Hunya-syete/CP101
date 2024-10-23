import random


secret_number = random.randint(1, 20)


tries = 0


max_tries = 3

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 20.")

while tries < max_tries:

    user_guess = input("Take a guess: ")


    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    tries += 1
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    elif user_guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")


if tries == max_tries:
    print(f"Sorry, you didn't guess the number. The number was {secret_number}.")
