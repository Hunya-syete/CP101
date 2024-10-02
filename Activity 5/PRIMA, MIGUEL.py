

strings = "My name is Miguel, I am 100 years old, I am from skypiya, and my favorite number is #^18"

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
specialCount = 0

for string in strings:
    if string.islower():
        lowercaseCount += 1
    elif string.isupper():
        uppercaseCount += 1
    elif string.isdigit():
        digitCount += 1
    else:
        specialCount += 1

print("Uppercase Letters:", uppercaseCount)
print("Lowercase Letters:", lowercaseCount)
print("Digits:", digitCount)
print("Special Characters:", specialCount)
