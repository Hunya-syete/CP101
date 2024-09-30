# Create a code that will count all lower case, upper case, digits, and special symbols from a given string.

string=("Hola! I am Mae Faith. 19 years old, living in Laoy Olingan. I'm currently taking up The Bachelor of Science in Information Technology. ")

lowerC = 0
upperC = 0
digitC = 0
specialC = 0

for F in string:
    if F.islower():
        lowerC = lowerC + 1
        
    elif F.isupper():
          upperC= upperC + 1
          
    elif F.isdigit():
          digitC = digitC + 1
          
    else:
           specialC = specialC + 1
           
print("Lower Count: ", lowerC)
print("Upper Count: ", upperC)
print("Digit Count:", digitC)
print("Special Count: ", specialC)
