def word_bank():
    words = []  

    while True:
        word = input("Enter a word: ")
        words.append(word) 

        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        
        if try_again.lower() == 'y':
            continue  
        elif try_again.lower() == 'n':
            break  
        else:
            print("Invalid input. Please enter Y/y or N/n.")

    print(f"\nYou entered a total of {len(words)} words.")
    print("The words you entered are:")
    for word in words:
        print(word)

word_bank()
