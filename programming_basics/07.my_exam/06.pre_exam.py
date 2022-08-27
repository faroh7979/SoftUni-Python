k = int(input())
l = int(input())
m = int(input())
n = int(input())
total_prints = 0
end = False

for first_player_first_num in range(k, 8 + 1):
    if end:
        break
    if first_player_first_num % 2 != 0:
        continue
    for first_player_second_num in range(9, l - 1, - 1):
        if end:
            break
        if first_player_second_num % 2 == 0:
            continue
        first_player_jersey = int(str(first_player_first_num)+str(first_player_second_num))
        for second_player_first_num in range(m, 8 + 1):
            if end:
                break
            if second_player_first_num % 2 != 0:
                continue
            for second_player_second_num in range(9, n - 1, - 1):
                if end:
                    break
                if second_player_second_num % 2 == 0:
                    continue
                second_player_jersey = int(str(second_player_first_num)+str(second_player_second_num))
                if first_player_jersey == second_player_jersey:
                    print("Cannot change the same player.")
                else:
                    print(f'{first_player_first_num}{first_player_second_num} - {second_player_first_num}{second_player_second_num}')
                    total_prints += 1
                if total_prints >= 6:
                    end = True
