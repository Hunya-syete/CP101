import random

number_to_guess = random.randint(1, 20)
attempts = 3

print("Hello! Welcome to 'Guess the Number'!")
print("Just think of a number between 1 and 20. You have free 3 attempts to guess it!")

for attempt in range(attempts):
    guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"VERY GOOD! You've guessed the number! {number_to_guess} correctly!")
        break
else:
    print(f"Oh no, you've used all your attempts. The number was {number_to_guess}. Better luck next time!")
