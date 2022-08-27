count_dancers = int(input())
count_points = float(input())
season = input()
location = input()
prize_money = 0

if location == 'Bulgaria':
    prize_money = count_dancers * count_points
    if season == 'summer':
        prize_money *= 0.95
    elif season == 'winter':
        prize_money *= 0.92
elif location == 'Abroad':
    prize_money = count_dancers *count_points
    prize_money *= 1.5
    if season == 'summer':
        prize_money *= 0.9
    elif season == 'winter':
        prize_money *= 0.85
charity_money = prize_money * 0.75
rest_money = prize_money - charity_money
money_per_dancer = rest_money / count_dancers

print(f'Charity - {charity_money:.2f}')
print(f'Money per dancer - {money_per_dancer:.2f}')
