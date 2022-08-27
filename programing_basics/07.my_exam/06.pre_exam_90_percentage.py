k = int(input())
l = int(input())
m = int(input())
n = int(input())
total_prints = 0
end = False

for first_player_first_num in range(k, 9):
    if end:
        break
    if first_player_first_num == 0:
        continue
    if first_player_first_num % 2 != 0:
        continue
    first_jersey_one = str(first_player_first_num)
    for first_player_second_num in range(9, l - 1, - 1):
        if end:
            break
        if first_player_second_num % 2 == 0:
            continue
        first_jersey_two = str(first_player_second_num)
        first_player_num = int(first_jersey_one + first_jersey_two)
        for second_player_first_num in range(m, 9):
            if end:
                break
            if second_player_first_num == 0:
                continue
            if second_player_first_num % 2 != 0:
                continue
            second_jersey_one = str(second_player_first_num)
            for second_player_second_num in range(9, n - 1, - 1):
                if end:
                    break
                if second_player_second_num % 2 == 0:
                    continue
                second_jersey_two = str(second_player_second_num)
                second_player_num = int(second_jersey_one + second_jersey_two)
                if first_player_num == second_player_num:
                    print('Cannot change the same player.')
                else:
                    print(f'{first_player_num} - {second_player_num}')
                    total_prints += 1
                if total_prints == 6:
                    end = True
