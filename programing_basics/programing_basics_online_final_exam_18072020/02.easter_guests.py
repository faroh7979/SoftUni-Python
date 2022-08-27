from math import ceil

number_of_guests = int(input())
budget_lubo = int(input())

price_sweet_bread_lv = 4
price_egg_lv = 0.45

needed_eggs = number_of_guests * 2
needed_sweet_breads = ceil(number_of_guests / 3)

total_expense = price_egg_lv * needed_eggs + price_sweet_bread_lv * needed_sweet_breads

difference = budget_lubo - total_expense

if difference >= 0:
    print(f"Lyubo bought {needed_sweet_breads:.0f} Easter bread and {needed_eggs:.0f} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(difference):.2f} lv. more.")
