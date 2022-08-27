one_lv_coin = int(input())
two_lv_coin = int(input())
five_lv_note = int(input())
total_sum = int(input())
customer_total = 0
one_lv_count = 0
two_lv_count = 0
five_lv_count = 0

for ones in range(0, one_lv_coin + 1):
    rested_sum = total_sum
    if ones != 0:
        rested_sum = rested_sum - ones
        one_lv_count = ones
    for twos in range(0, two_lv_coin + 1, 2):
        if twos != 0:
            rested_sum = rested_sum - (twos * 2)
            two_lv_count = twos / 2
        for fives in range(0, five_lv_note + 1, 5):
            if fives == 0:
                if rested_sum == 0:
                    print(f'{one_lv_count:.0f} * 1 lv. + {two_lv_count:.0f} * 2 lv. + {five_lv_count:.0f} * 5 lv. = {total_sum} lv.')
                    continue
                else:
                    continue
            rested_sum = rested_sum - (fives * 5)
            five_lv_count = fives % rested_sum
            if rested_sum == 0:
                print(f'{one_lv_count:.0f} * 1 lv. + {two_lv_count:.0f} * 2 lv. + {five_lv_count:.0f} * 5 lv. = {total_sum} lv.')
