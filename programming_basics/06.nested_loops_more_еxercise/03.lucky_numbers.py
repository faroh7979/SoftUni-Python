lucky_num = int(input())
first_two_sum = 0
second_two_sum = 0

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):
                first_first_two_sum = first_digit + second_digit
                second_two_sum = third_digit + fourth_digit
                if first_first_two_sum != second_two_sum:
                    continue
                if lucky_num % first_first_two_sum != 0:
                    continue
                print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')
