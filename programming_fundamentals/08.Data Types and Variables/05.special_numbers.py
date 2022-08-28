bound_nums = int(input())
current_sum = 0

for current_num in range(1, bound_nums + 1):
    for index, digit in enumerate(str(current_num)):
        current_sum += int(digit)
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f'{current_num} -> True')
    else:
        print(f'{current_num} -> False')
    current_sum = 0