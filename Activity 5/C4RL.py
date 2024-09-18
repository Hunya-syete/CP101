def carldev(c):

    lower_case = 0
    upper_case = 0
    digit_count = 0
    special_char = 0

    for almightyc4rl in c:

        if almightyc4rl.islower():
            lower_case += 1

        elif almightyc4rl.isupper():
            upper_case += 1

        elif almightyc4rl.isdigit():
            digit_count += 1

        else:
            special_char += 1

    print("Lowercase letters: ", lower_case)
    print("Uppercase letters: ", upper_case)
    print("Digits: ", digit_count)
    print("Special Characters: ", special_char)


carlString = "Si Carl Ay Pogi At Hindi Pangit #_#@@12345678910"

carldev(carlString)