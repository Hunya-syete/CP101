import random

def guess_the_number():
  """A simple "Guess the Number" game."""

  random_number = random.randint(1, 20)
  attempts = 3

  while attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess == random_number:
      print("Congratulations! You guessed the number.")
      return
    elif guess > random_number:
      print("Your guess is too high.")
    else:
      print("Your guess is too low.")

    attempts -= 1

  print("Sorry, you ran out of attempts. The number was", random_number)

guess_the_number()
