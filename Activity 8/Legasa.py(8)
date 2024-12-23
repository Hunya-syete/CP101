import random

def guess_the_number():
 
    number_to_guess = random.randint(1, 20)
    attempts = 3  

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Congratulations! You've guessed the number!")
            break  

    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
