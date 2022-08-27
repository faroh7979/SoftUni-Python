interval_start = int(input())
interval_end = int(input())

for first_num in range(interval_start, interval_end + 1):
    for second_num in range(interval_start, interval_end + 1):
        for third_num in range(interval_start, interval_end + 1):
            for fourth_num in range(interval_start, interval_end + 1):
                if (first_num % 2 == 0 and fourth_num % 2 == 0) or (first_num % 2 != 0 and fourth_num % 2 != 0):
                    continue
                if first_num <= fourth_num:
                    continue
                if (second_num + third_num) % 2 != 0:
                    continue
                print(f'{first_num}{second_num}{third_num}{fourth_num}', end=' ')
