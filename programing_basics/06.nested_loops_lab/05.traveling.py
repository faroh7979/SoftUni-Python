country = ''
needed_money = 0
save = 0
total_saves = 0
while country != 'End':
    country = input()
    if country == 'End':
        break
    needed_money = float(input())
    total_saves = 0
    while needed_money > total_saves:
        save = float(input())
        total_saves += save
        if needed_money <= total_saves:
            print(f'Going to {country}!')
            break
