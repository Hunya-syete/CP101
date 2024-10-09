# Initialize an empty list to store words
wordOfBank = []

# Welcome message
print("HELLO, WELCOME TO MY SITE, AS YOU CAN SEE PWEDE KA MAG LAGAY NG KAHIT ANONG WORD DITO! ENJOY :)")

print("\n") # Add a newline for better spacing


# Loop to collect words from the user
while True:

    wrd = input("\nENTER YOUR ANY WORDS: ") # Prompt user for a word
    
    wordOfBank.append(wrd)  # Add the word to the list
    
    
    # Ask user if they want to add more words
    add_word = input("\nDO YOU WANT TO ADD MORE WORDS? [Y/N]: ")
        
    if add_word == "Y" or add_word =="y":  #If yes, continue the loop
        pass
        
    else: # If no, break the loop
        break

# Print the total number of words collected
print(f"\nTOTAL OF WORDS ON THE LIST: {len(wordOfBank)}")

# Print the list of words
print("\nLIST OF WORDS IN THE WORD OF BANK: ")



i = 1
# Loop through each word in the list and print it

for word in wordOfBank:
    print()  # Add a newline for better spacing
    print("LIST OF WORD #" + str(i)) # Print the word number
    print(word) # Print the word itself
    i += 1 # Increment the counter
