# Given string
text = "Hi my name is $Jommil$ i love ?burger? and playing /Minecraft/"

# Initialize counters
lowercase_count = 0
uppercase_count = 0
digit_count = 0
special_count = 0

# Loop through each character in the string and count each type
for char in text:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isalnum() and not char.isspace():  # Special characters (excluding spaces)
        special_count += 1

# Display the results
print("Results:")
print(f"Lowercase letters: {lowercase_count}")
print(f"Uppercase letters: {uppercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")
