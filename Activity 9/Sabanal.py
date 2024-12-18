def word_bank_program():
    
    word_list = []
    
    while True:
        
        word = input("Enter a word: ")
        
        word_list.append(word)
        
        
        try_again = input("Do you want to try again? (Y/y for Yes, N/n for No): ").strip().lower()
        
        
        if try_again == 'n':
            print(f"\nTotal number of words: {len(word_list)}")
            print("Words entered:", ", ".join(word_list))
            break
        elif try_again != 'y':
            print("Invalid input. Please enter Y/y or N/n.")


word_bank_program()
