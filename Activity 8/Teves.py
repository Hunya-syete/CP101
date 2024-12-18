():
print("Welcome to 'Guess the Number'!")
    print("I have chosen a number between 1 and 20. Can you guess it?")

    number_to_guess = random.randint(1, 20)
    attempts_left = 3

    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))

            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            if guess == number_to_guess:
                print(f"Well done! You guessed it right. The number was {number_to_guess}.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            attempts_left -= 1

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts_left == 0:
        print(f"Out of attempts! The correct number was {number_to_guess}. Better luck next time!")

play_guess_the_number()
