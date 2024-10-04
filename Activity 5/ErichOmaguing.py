text = input("Enter a text: ")

lower_count = 0
upper_count = 0
s_char_count = 0
digit = 0

for letter in text:
    if letter.islower():
        lower_count += 1
    elif letter.isupper():
        upper_count += 1
    elif letter.isdigit():
        digit += 1
    else:
        s_char_count += 1
        
print("lower case count is: ", lower_count)
print("upper case counr is: ", upper_count)
print("digit count is: ", digit)
print("special character count is: ", s_char_count)
