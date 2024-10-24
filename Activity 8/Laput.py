import random

secret_number = random.randint(1, 20)
max_attempts = 3

print("Welcome to the Guess the Number game!")
print("I have picked a number between 1 and 20.")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: What's your guess? "))

    if guess == secret_number:
        print(f"Well done! You guessed the number {secret_number} in {attempt} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    if attempt == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}."
