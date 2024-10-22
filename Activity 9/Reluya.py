def word_bank_program():
    words = []  # Initialize an empty list to store words

    while True:
        # Ask the user to enter a word
        word = input("Enter a word: ")
        words.append(word)  # Store the word in the list

        # Ask if the user wants to try again
        repeat = input("Do you want to enter another word? (Y/y for Yes, any other key for No): ")

        if repeat.lower() != 'rod':
            break  # Exit the loop if the user chooses not to continue

    # Display the total number of words and the words entered
    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:")
    for word in words:
        print(word)

# Run the program
word_bank_program()
