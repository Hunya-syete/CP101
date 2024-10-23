def word_bank():
    words = []
    while True:
       
        word = input("Enter a word: ")
        words.append(word)  
        
        try_again = input("Do you want to try again? (Y/y for Yes, N/n for No): ").lower()
        
        if try_again == 'n':  
            print(f"\nTotal number of words: {len(words)}")
            print("Words entered:", words)
            break
        elif try_again != 'y':  
            print("Invalid input. Exiting the program.")
            break

word_bank()
