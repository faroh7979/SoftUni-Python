def password_validation(user: str):
    numeric_count = 0
    long_enough = True
    alphabetic = True
    at_least_two_digits = True
    if len(user) < 6 or len(user) > 10:
        long_enough = False
    for current_char_one in user:
        if not current_char_one.isalpha() and not current_char_one.isnumeric():
            alphabetic = False
            break
    for current_char in user:
        if current_char.isnumeric():
            numeric_count += 1
    if numeric_count < 2:
        at_least_two_digits = False
    if long_enough and alphabetic and at_least_two_digits:
        print("Password is valid")
    else:
        if not long_enough:
            print("Password must be between 6 and 10 characters")
        if not alphabetic:
            print("Password must consist only of letters and digits")
        if not at_least_two_digits:
            print("Password must have at least 2 digits")


user_password = input()
password_validation(user_password)
