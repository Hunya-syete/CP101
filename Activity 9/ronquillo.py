# Word bank program

# Initialize an empty word bank (a list to store words)
word_bank = []

def display_menu():
    print("\n--- Word Bank Menu ---")
    print("1. Add a word")
    print("2. View all words")
    print("3. Search for a word")
    print("4. Exit")

def add_word():
    word = input("Enter a word to add to the word bank: ")
    word_bank.append(word)
    print(f"'{word}' has been added to the word bank.")

def view_words():
    if word_bank:
        print("\nWords in the word bank:")
        for word in word_bank:
            print(f"- {word}")
    else:
        print("The word bank is empty.")

def search_word():
    word = input("Enter a word to search: ")
    if word in word_bank:
        print(f"'{word}' is in the word bank.")
    else:
        print(f"'{word}' is not found in the word bank.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_word()
        elif choice == '2':
            view_words()
        elif choice == '3':
            search_word()
        elif choice == '4':
            print("Exiting the word bank program.")
            break
        else:
            print("Invalid choice. Please try again.")

def try_again():
    while True:
        again = input("Do you want to try again? (Y/y for Yes, N/n for No): ").lower()
        if again == 'y':
            main()  # Restart the program
            break  # Exit the loop to prevent multiple restarts
        elif again == 'n':
            print("Goodbye!")
            # Display total number of words and all entered words
            print(f"Total number of words: {len(word_bank)}")
            if word_bank:
                print("Words in the word bank:")
                for word in word_bank:
                    print(f"- {word}")
            break  # Exit the loop and end the program
        else:
            print("Invalid input. Please enter Y/y or N/n.")

# Run the program
if __name__ == "__main__":
    main()
    try_again()
