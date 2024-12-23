import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 3

    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < 1 or guess > 20:
            print("Your guess is out of range! Please guess a number between 1 and 20.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
    else:
        print(f"Sorry! You've used all your attempts. The correct number was {number_to_guess}.")

guess_the_number()
