word_list = []  
# Create an empty list to store the words

while True:  
# Start an infinite loop
  word = input("Enter a word: ")
  word_list.append(word)  
# Add the entered word to the list

  again = input("Do you want to try again? (Y/N): ")  
# Ask if the user wants to continue

  if again.upper() == 'N':  
# Check if the user wants to stop
    break  
# Exit the loop if the user enters 'N' or 'n'

print("Total number of words:", len(word_list))  
# Display the total number of words
print("Words entered:", word_list)  
# Display all the words entered
