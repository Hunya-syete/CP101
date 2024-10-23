class WordBank:
    
    def __init__(self):
        
        self.wordOfBank = []
        print("HELLO, WELCOME TO MY SITE! ENJOY :)")
        self.collect_words()

    def collect_words(self):
        
        while True:
            
            word = input("\nENTER ANY WORD: ")
            
            if word.strip():
                
                self.wordOfBank.append(word)
                
                if input("\nDO YOU WANT TO ADD MORE WORDS? [Y/N]: ").strip().lower() != 'y':
                    break
            else:
                
                print("Please enter a valid word.")
                
        self.display_words()
        

    def display_words(self):
        
        print(f"\nTOTAL OF WORDS ON THE LIST: {len(self.wordOfBank)}")
        
        print("\nLIST OF WORDS IN THE WORD OF BANK:")
        
        for i, word in enumerate(self.wordOfBank, start=1):
            print(f"\nLIST OF WORD #{i}: {word}")

WordBank()
