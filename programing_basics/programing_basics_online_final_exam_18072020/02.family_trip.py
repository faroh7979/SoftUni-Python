budget = float (input())
nights = int(input())
price_per_night = float(input())
additional_expense_percentage = int(input())

over_7_night_discount_percentage = 5

if nights > 7:
    price_per_night = price_per_night - price_per_night * over_7_night_discount_percentage / 100
else:
    price_per_night = price_per_night

total_expense = price_per_night * nights + budget * additional_expense_percentage / 100

difference = budget - total_expense
differencef = "{:.2f}".format(difference)

needed_add_money = total_expense - budget
needed_add_moneyf = "{:.2f}".format(needed_add_money)

if difference >= 0:
    print(f"Ivanovi will be left with {differencef} leva after vacation.")
else:
    print(f"{needed_add_moneyf} leva needed.")

