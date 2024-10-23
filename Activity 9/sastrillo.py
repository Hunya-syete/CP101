words = []


while True:
    word = input("Enter a word: ")
    words.append(word)


    again = input("Do you want to enter another word? (YES/NO): ")


    if again.upper() == "NO":
        break


print("\nYou entered", len(words), "words.")
print("Here are the words you entered:")
for word in words:
    print(word)
