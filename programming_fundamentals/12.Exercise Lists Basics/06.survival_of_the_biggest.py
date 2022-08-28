from sys import maxsize as ms

list_of_integer = input().split(' ')
removed_numbers = int(input())

for _ in range(removed_numbers):
    min_num = ms
    for current_int in list_of_integer:
        if int(current_int) < min_num:
            min_num = int(current_int)
    list_of_integer.remove(str(min_num))
for current_index in range(len(list_of_integer)):
    current_num = int(list_of_integer[current_index])
    if current_index == len(list_of_integer) - 1:
        print(current_num)
    else:
        print(f"{current_num}, ", end='')
