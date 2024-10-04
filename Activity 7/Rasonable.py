def count_characters(string):
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0
   
    for char in string:
        if char.islower():
            lowercase_count+= 1
        elif char.isupper():
            uppercase_count+= 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1
            
    return lowercase_count, uppercase_count, digit_count, special_count
    
  
input_string = "Alan Lloyd N. Rasonable  18 years old lived in Sta.Cruz Dipolog City born in March 27,2006."
lowercase, uppercase, digits, special = count_characters(input_string)

print(f"{input_string}")
print(f"Lowercase): {lowercase}")
print(f"Uppercase): {uppercase}")
print(f"Digit): {digits}")
print(f"Special Symbol): {special}")
