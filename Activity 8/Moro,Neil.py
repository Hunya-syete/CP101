import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 3
    
    print("Guess a number between 1 to 20.")
    
    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
        
        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < number_to_guess:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
    
    if guess != number_to_guess:
        print(f"Sorry, you have used all your attempts. The number was {number_to_guess}.")

guess_the_number()
