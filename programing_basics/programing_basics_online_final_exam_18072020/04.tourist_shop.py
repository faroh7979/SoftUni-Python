budget = float(input())
total_expense = 0
product_name = ''
single_price = 0
enough_money = False
bought_products = -1
product_order = 0
while total_expense <= budget:
    bought_products += 1
    product_name = input()
    if product_name == "Stop":
        enough_money = True
        break
    single_price = float(input())
    product_order += 1
    if product_order % 3 == 0:
        single_price /= 2
    total_expense += single_price
if enough_money:
    print(f'You bought {bought_products} products for {total_expense:.2f} leva.')
else:
    difference = total_expense - budget
    print("You don't have enough money!")
    print(f'You need {difference:.2f} leva!')
