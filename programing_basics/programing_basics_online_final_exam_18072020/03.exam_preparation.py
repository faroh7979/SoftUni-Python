movie_budget = float(input())
destination = input()
season = input()
days_needed = int(input())
daily_needed_money = 0
if destination == 'Dubai':
    if season == 'Winter':
        daily_needed_money = 45000
    elif season == 'Summer':
        daily_needed_money = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        daily_needed_money = 17000
    elif season == 'Summer':
        daily_needed_money = 12500
elif destination == 'London':
    if season == 'Winter':
        daily_needed_money = 24000
    elif season == 'Summer':
        daily_needed_money = 20250
if destination == 'Dubai':
    daily_needed_money *= 0.7
elif destination == 'Sofia':
    daily_needed_money *= 1.25
total_expense = days_needed * daily_needed_money
difference = abs(movie_budget - total_expense)

if total_expense <= movie_budget:
    print(f'The budget for the movie is enough! We have {difference:.2f} leva left!')
else:
    print(f'The director needs {difference:.2f} leva more!')
