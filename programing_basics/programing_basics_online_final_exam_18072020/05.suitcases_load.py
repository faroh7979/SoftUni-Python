truck_capacity = float(input())
total_used_volume = 0
total_suitcases = 0

while truck_capacity > total_used_volume:
    suitcase_volume = input()
    if suitcase_volume == 'End':
        break
    suitcase_volume = float(suitcase_volume)
    total_suitcases += 1
    if total_suitcases % 3 == 0:
        suitcase_volume = suitcase_volume * 1.1
    total_used_volume += suitcase_volume
if truck_capacity >= total_used_volume:
    print('Congratulations! All suitcases are loaded!')
    print(f'Statistic: {total_suitcases} suitcases loaded.')
else:
    print('No more space!')
    print(f'Statistic: {total_suitcases - 1} suitcases loaded.')
