def word_bank():
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        if input("Try again? (Y/y for Yes, N/n for No): ").lower() not in ['y', 'yes']:
            break

    print(f"\nYou entered {len(words)} words: {', '.join(words)}")

# Run the word bank program
word_bank()
