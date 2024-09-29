string=("Anneyong! My name is Jamaica Tumanao, 18 years old, born in January 29,2006,jamaicatumanao@gmail.com")

lowercase = 0
uppercase = 0
digitcase = 0
specialcase = 0

for J in string:
    if J.islower():
         lowercase = lowercase + 1
        
    elif J.isupper():
        uppercase = uppercase + 1
      
    elif J.isdigit():
        digitcase = digitcase + 1
        
    else:
        specialcase = specialcase + 1
        
print("Lower Count: ", lowercase)
print("Upper Count: ", uppercase)
print("Digit Count: ", digitcase)
print("Special Count: ", specialcase)
