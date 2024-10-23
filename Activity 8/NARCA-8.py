import random

class GuessTheNumber:
    
    def __init__(self):
        
        self.number_to_guess = random.randint(1, 20)
        self.attempts = 3

    def play(self):
        
        print("\nGuess the number between 1 and 20! You have 3 attempts.")
        
        for attempt in range(self.attempts):
            
            guess = int(input("\nEnter your guess: "))
            
            if guess == self.number_to_guess:
                
                print("Wow, You guess It!!")
                break
            
            elif guess > self.number_to_guess:
                print("Too High!")
                
            elif guess < self.number_to_guess:
                
                print("Too low!")
                
        else:
            
            print(f"\nThe number was {self.number_to_guess}")
            
shiela = GuessTheNumber()
shiela.play()
