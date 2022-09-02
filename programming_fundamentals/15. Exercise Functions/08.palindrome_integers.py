def is_palindrome(user_input: list):
    for current_num in user_input:
        if str(current_num)[0] == str(current_num)[-1]:
            print(True)
        else:
            print(False)


client_list = list(map(int, input().split(', ')))
is_palindrome(client_list)
