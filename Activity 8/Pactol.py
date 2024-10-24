import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    print("Guess the number between 1 and 20. You have 3 attempts.")

    for attempt in range(3):
        guess = int(input(f"Attempt {attempt + 1}: "))
        if guess == secret_number:
            print(f"Congratulations! You've guessed it: {secret_number}.")
            break
        print("Too low." if guess < secret_number else "Too high.")
    else:
        print(f"Sorry, the correct number was {secret_number}.")

guess_the_number()
