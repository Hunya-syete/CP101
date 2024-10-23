import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 3  

    print("Welcome to 'HULA-HULAAN'!")
    print("I have selected a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(attempts):
        try:
            guess = int(input(f"Attempt {attempt + 1}: Your guess? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 20:
            print("Your guess is out of bounds! Please guess a number between 1 and 20.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt + 1} attempts.")
            break
    else:
        print(f"Sorry! 3 times ra pwede mag guess. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
