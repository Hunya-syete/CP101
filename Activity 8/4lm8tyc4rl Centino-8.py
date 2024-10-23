import random

class GuessTheNumber:

    def __init__(self, number, attempts=3):  

        self.number = random.randint(1, number) 
        self.attempts = attempts

    def play(self):

        print(f"GUESS THE NUMBER BETWEEN 1 AND {number}. YOU HAVE {self.attempts} ATTEMPTS! OKAY?")

        for _ in range(self.attempts):

            guess = int(input("\nENTER YOUR GUESS: "))

            if guess == self.number:
                print("WOW!! AMAZING! YOU GOT IT!!")
                break

            elif guess > self.number:
                print("TOO HIGH!")

            elif guess < self.number:
                print("TOO LOW!")

        else:
            print(f"\nTHE NUMBER WAS {self.number}.")

while True:

    number = 20
    game = GuessTheNumber(number)
    game.play()

    add_play_again = input("\nDO YOU WANT TO PLAY AGAIN? [Y/N]: ").lower()

    if add_play_again == "Y" or add_play_again == "y":
        pass

    else:
        break
