shielaString = "GOodLuCk  on OuR MIdteRm Exam200504@#"

lowercase = 0
uppercase = 0
digitcount = 0
specialcharacters = 0

for i in shielaString:
	if i.islower():
		lowercase = lowercase + 1
		
	elif i.isupper():
		uppercase = uppercase + 1
	
	elif i.isdigit():
		digitcount = digitcount + 1
		
	else:
		specialcharacters = specialcharacters + 1
	
print("Lowercase letters: ", lowercase)

print("Uppercase letters: ", uppercase)

print("Digits: ", digitcount)

print("Special Characters: ", specialcharacters)
