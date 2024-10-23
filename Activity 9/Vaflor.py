def word_bank():
    words = []  

    while True:
        word = input("Enter a word: ").strip()  

        
        if word in words:
            print("This word is already in the list. Please enter a different word.")
        else:
            words.append(word)  
            print(f"'{word}' has been added to the word bank.")

        
        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        
        if try_again.lower() == 'n':  
            break  

    
    while True:
        remove_word = input("Do you want to remove a word from the list? (Y/y for Yes, N/n for No): ")
        if remove_word.lower() == 'y':
            word_to_remove = input("Enter the word you want to remove: ").strip()
            if word_to_remove in words:
                words.remove(word_to_remove)
                print(f"'{word_to_remove}' has been removed from the word bank.")
            else:
                print("This word is not in the list.")
        elif remove_word.lower() == 'n':
            break

    
    print(f"\nTotal number of words entered: {len(words)}")
    print("Words entered:")
    for word in words:
        print(word)

if __name__ == "__main__":
    word_bank()
