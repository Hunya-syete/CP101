import random

def game():

    random_num = random.randrange(1, 21)

    print ("\n\033[92mLETS PLAY A GAME! \n\033[0mYou have three attempts to guess the random number from (\033[93m1 - 20\033[0m).")

    for i in range(3):
        while True:
            try:
                guess = int(input(f"\n\033[92mAttempt {i+1}: \n\033[0mGuess the number: "))
                if 1 <= guess <= 20:
                    break
                else:
                    print("Invalid, just number ranging 1 - 20")
            except ValueError:
                print ("Invalid, integer only 1 - 20")

        if guess == random_num:
            print ("\n\033[93mCongratulations! \n\033[0mYou guessed the right number")
            break
        elif i < 2:
            if guess > random_num:
                print ("Try a lower number")
            else:
                print ("Try a higher number")

    if guess != random_num:
        print (f"\n\033[91mBetter Luck Next Time!\033[0m\nThe random number was {random_num}.")

def play_again():
    while True:
        play_again = input("\n\033[95mWould you like to play again? \033[0m\033[93m(yes/no)\033[0m:").strip().lower()
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print ("Invalid, just yes/no or YES/NO")

while True:
    game()
    if not play_again():
        print ("\n\033[93mThank you for playing!\033[0m")
        break
