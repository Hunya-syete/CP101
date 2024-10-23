import random

number_to_guess = random.randint(1, 20)

max_attempts = 3

print("Welcome to 'Guess the Number'!")
print("I have selected a number between 1 and 20. You have 3 attempts to guess it.")

for attempt in range(1, max_attempts + 1):
   
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempt} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")

    if attempt == max_attempts:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")
5
