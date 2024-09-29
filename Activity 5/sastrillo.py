def count_characters(s):
    lower_case_count = sum(1 for char in s if char.islower())
    upper_case_count = sum(1 for char in s if char.isupper())
    digit_count = sum(1 for char in s if char.isdigit())
    special_count = sum(1 for char in s if not char.isalnum())

    return {
        "lower_case": lower_case_count,
        "upper_case": upper_case_count,
        "digits": digit_count,
        "special_symbols": special_count}
        
kian_string = "hi hello, my name is kian, 19 years old na ako po at nag aaral sa svci 12728@--371+@&AqWUQJAJSDOUQ"
result = count_characters(kian_string)
print(result)

{'lower_case': 51, 'upper_case': 12, 'digits': 10, 'special_symbols': 25}



=== Code Execution Successful ===
