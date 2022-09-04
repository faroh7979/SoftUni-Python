version = list(map(int, input().split('.')))

first_num = version[0]
second_num = version[1]
third_num = version[2]
if third_num == 9:
    third_num = 0
    second_num += 1
    if second_num == 10:
        second_num = 0
        first_num += 1
else:
    third_num += 1
print(f'{first_num}.{second_num}.{third_num}')
