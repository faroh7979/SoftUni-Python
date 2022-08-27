client_num = int(input())

for row in range(1, client_num + 1):
    if row == 1 or row == client_num:
        for column in range(1, client_num + 1):
            if column == 1 or column == client_num:
                print('+', end=" ")
            else:
                print('-', end=" ")
        print()
    else:
        for column in range(1, client_num + 1):
            if column == 1 or column == client_num:
                print('|', end=" ")
            else:
                print('-', end=" ")
        print()
