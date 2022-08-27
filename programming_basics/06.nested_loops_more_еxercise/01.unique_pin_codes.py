first_num_up_to = int(input())
second_num_up_to = int(input())
third_num_up_to = int(input())
is_prime = True

for first_num in range(1, first_num_up_to + 1):
    if first_num % 2 != 0:
        continue
    for second_num in range(2, second_num_up_to + 1):
        is_prime = True
        if second_num != 2:
            for divider in range(2, second_num):
                if second_num != 2:
                    if second_num % divider == 0:
                        is_prime = False
                        break
        if not is_prime:
            continue
        for third_num in range(1, third_num_up_to + 1):
            if third_num % 2 != 0:
                continue
            print(f'{first_num} {second_num} {third_num}')
