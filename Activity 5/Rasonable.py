alan_string = "SI ALAN AY TAMAD $###$$$!!!"

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
specialCount = 0

for alan in alan_string:
    if alan.islower():
        lowercasecount += 1
    elif alan.isupper():
        uppercaseCount += 1
    elif alan.isdigit():
        digitCount += 1
    else:
        specialCount += 1
        
print("Lowercase letters:", lowercaseCount)
print("Uppercase letters:", uppercaseCount)
print("Digits:", digitCount)
print("Special Characters:", specialCount)
