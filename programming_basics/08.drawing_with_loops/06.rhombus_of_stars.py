client_num = int(input())
decrease = client_num - 1
increase = 1

for spaces in range(client_num):
    if client_num != 1:
        print(' ' * decrease + '* ' * (spaces + 1))
    else:
        print(' ' * decrease + '* ' * (spaces + 1), end='')
    decrease -= 1
for dec_spaces in range(client_num - 1, 0, -1):
    if dec_spaces != 1:
        print(' ' * increase + '* ' * dec_spaces)
    else:
        print(' ' * increase + '* ' * dec_spaces, end='')
    increase += 1
