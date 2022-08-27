start_interval = int(input())
end_interval = int(input())
magical_number = int(input())
total_combinations = 0
founded_combination = False
for first_num in range(start_interval, end_interval + 1):
    if founded_combination:
        break
    for second_num in range(start_interval, end_interval + 1):
        if founded_combination:
            break
        total_combinations += 1
        if first_num + second_num == magical_number:
            founded_combination = True
            print(f'Combination N:{total_combinations} ({first_num} + {second_num} = {magical_number})')
if not founded_combination:
    print(f'{total_combinations} combinations - neither equals {magical_number}')
