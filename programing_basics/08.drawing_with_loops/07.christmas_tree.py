client_num = int(input())
decrease = client_num
for tree in range(1, client_num + 2):
    print(' ' * decrease + '*' * (tree - 1) + ' | ' + '*' * (tree-1))
    decrease -= 1
