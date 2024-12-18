import string

# Function to count upper case, lower case, digits, and special symbols
def count_chars(text):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    symbol_count = 0
    
    for char in text:
        if char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.digits:
            digit_count += 1
        elif char in string.punctuation:
            symbol_count += 1
        elif char.isspace():
            continue  # Ignoring spaces

    return upper_count, lower_count, digit_count, symbol_count

# Input string
text = " Hey there, My name is Shawn Michael Sabanal 17yrs old, dreaming that someday that I will be a profeesional IT soon."

# Counting characters
upper, lower, digits, symbols = count_chars(text)

# Displaying the results
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Special symbols:", symbols)
