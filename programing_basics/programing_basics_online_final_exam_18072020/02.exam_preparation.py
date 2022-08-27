budget = float(input())
total_nights = int(input())
price_single_night = float(input())
percentage_additional_expense = int(input())

if total_nights > 7:
    price_single_night *= 0.95
total_host_expense = total_nights * price_single_night
additional_expense = budget * percentage_additional_expense / 100
total_expense = total_host_expense + additional_expense
difference = abs(budget - total_expense)

if total_expense <= budget:
    print(f'Ivanovi will be left with {difference:.2f} leva after vacation.')
else:
    print(f'{difference:.2f} leva needed.')
