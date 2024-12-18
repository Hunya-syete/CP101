import random

number_to_guess = random.randint(1, 20)
attempts = 3

print("Guess the number between 1 and 20. You have 3 attempts!")

# looping
for attempt in range(attempts):
    guess = int(input(f"Attempt {attempt + 1}: Your guess: "))
    
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Oopsie! The correct number was {number_to_guess};))")
