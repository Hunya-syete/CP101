import random

secret_number = random.randint(1, 20)  
# Generate a random number
attempts = 3  
# Set the number of attempts

print("I'm thinking of a number between 1 and 20.")

for i in range(attempts):
  guess = int(input("Take a guess: "))

  if guess == secret_number:
    print("Congratulations! You guessed it in", i + 1, "attempts.")
    break  
# End the game if the guess is correct

  elif guess < secret_number:
    print("Too low! Try again.")

  else:
    print("Too high! Try again.")

if guess != secret_number:
  print("Sorry, you ran out of attempts. The number was", secret_number)
