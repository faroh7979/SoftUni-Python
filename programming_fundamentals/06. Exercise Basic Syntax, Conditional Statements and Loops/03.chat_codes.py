total_numbers = int(input())

for _ in range(total_numbers):
    phone_num = int(input())
    if phone_num == 88:
        print('Hello')
    elif phone_num == 86:
        print('How are you?')
    elif phone_num < 88:
        print('GREAT!')
    elif phone_num > 88:
        print('Bye.')
