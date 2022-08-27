first_num = int(input())
second_num = int(input())
magic_num = int(input())
total = ''
discovered_combination = False
order = 0
combination1 = ''
combination2 = ''
for combination1 in range(first_num, second_num + 1):
    for combination2 in range(first_num, second_num + 1):
        total = combination1 + combination2
        order += 1
        if total == magic_num:
            discovered_combination = True
            break
    if discovered_combination:
        break
if discovered_combination:
    print(f'Combination N:{order} ({combination1} + {combination2} = {magic_num})')
else:
    print(f'{order} combinations - neither equals {magic_num}')
