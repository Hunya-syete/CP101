import random

def guess_the_number():
    
    number_to_guess = random.randint(1, 20)
    attempts = 3 

    print("Welcome to 'Guess the Number'!")
    print("I am thinking of a number between 1 and 20.")

    
    for attempt in range(attempts):
        
        guess = int(input(f"Attempt {attempt + 1}/{attempts}: Take a guess: "))

      
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess}.")
            break  
    else:
        
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")


guess_the_number()
