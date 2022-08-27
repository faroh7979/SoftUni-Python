budget = float(input())
count_static = int(input())
static_outfit_price = float(input())
decor = budget * 0.1

if count_static > 150:
    static_outfit_price = static_outfit_price * 0.9

else:
    static_outfit_price = static_outfit_price

total = count_static * static_outfit_price + decor

need_more_money = total - budget
need_more_moneyf = "{:.2f}".format(need_more_money)
charge = budget - total
chargef = "{:.2f}".format(charge)

totalf = "{:.2f}".format(total)

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {need_more_moneyf} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {chargef} leva left.")
