string=("Hello!! iam Marchel Alia BSIT student 1st year Batch 2024 that's all thank you.")

lowerC = 0
upperC = 0
digitC = 0
specialC = 0

for M in string:
    if M.islower():
        lowercase = lowerC + 1
        
    elif M.isupper():
        upperC = upperC + 1
        
    elif M.isdigit():
        digitC = digitC + 1
        
    else:
           specialC = specialC + 1
          
print("Lower Count: ", lowerC)
print("Upper Count: ", upperC)
print("Digit Count: ", digitC)
print("Special Count: ", specialC)
