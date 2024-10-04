String = "My Name is Ivan Vincent Alimpulos,Age 18,and I like to play Mobilelegends."

lowercase_count = 0
uppercase_count = 0
digit_count = 0
special_count = 0

for ivan in String:
	if ivan.islower():
		lowercase_count += 1
	elif ivan.isupper():
		uppercase_count += 1
	elif ivan.isdigit():
		digit_count += 1
	elif not ivan.isspace():
	   
		special_count += 1
	
print("Lowercase letters: ", lowercase_count)
print("Uppercase letters: ", uppercase_count)
print("Digits: ", digit_count)
print("Special Characters: ", special_count)
