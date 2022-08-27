budget = float(input())
need_liters_fuel = float(input())
weekly_day = input()

fuel_price_liter = 2.10
gid_leva = 100

if weekly_day == "Saturday":
    discount = 0.1
else:
    discount = 0.2

total_expense = need_liters_fuel * fuel_price_liter + gid_leva
discounted_price = total_expense - total_expense * discount

rested_money = budget - discounted_price
rested_moneyf = "{:.2f}".format(rested_money)

needed_money = discounted_price - budget
needed_moneyf = "{:.2f}".format(needed_money)

if rested_money >= 0:
    print(f"Safari time! Money left: {rested_moneyf} lv.")
else:
    print(f"Not enough money! Money needed: {needed_moneyf} lv.")
