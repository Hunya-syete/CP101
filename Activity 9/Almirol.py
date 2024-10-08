word_bank = []

print ("\n\033[95mHi! You can add words as much as you can. \nLet's go!\033[0m")

while True:

    word = str(input("\n\033[92mEnter your choice of word\033[0m: "))
    word_bank.append(word)

    while True:

        add_word = input("\n\033[92mWould you like to add more word\033[0m?\n(\033[95mY/y\033[0m if yes, \033[95mN/n\033[0m if no): ").strip().lower()

        if add_word in ["y", "n"]:
            break
        else:
            print ("\033[91mInvalid!\033[0m Enter Y/y for YES and N/n for NO")

    if add_word == "n":
            break

print (f"\n\033[93mTotal of words on the list\033[0m: {len(word_bank)}")
print ("\n\033[93mList of words in the word bank\033[0m:")

for word in word_bank:
    print (word)
