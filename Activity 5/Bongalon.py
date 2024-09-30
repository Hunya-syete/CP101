Massages = "Greetings!!, # I am HUNTER CODE BlAcK@ 11, Password is *11-02-9999*."


lowercase = 0
uppercase = 0
digits = 0
special_symbols = 0


for Massage in Massages:
    if Massage.islower():
        lowercase += 1
    elif Massage.isupper():
        uppercase += 1
    elif Massage.isdigit():
        digits += 1
    else:
        special_symbols += 1
        
        
print ("Lowercase:", lowercase)
print ("Uppercase:", uppercase)
print ("Digits:", digits)
print ("Special_symbols:", special_symbols)
