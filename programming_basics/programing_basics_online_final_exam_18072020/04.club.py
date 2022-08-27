needed_incomes = float(input())
total_incomes = 0
single_order_price = 0
drink_price = 0
enough_money = True
while total_incomes < needed_incomes:
    drink_name = input()
    if drink_name == 'Party!':
        enough_money = False
        break
    count_drinks = int(input())
    drink_price = int(len(drink_name))
    single_order_price = drink_price * count_drinks
    if single_order_price % 2 == 1:
        single_order_price *= 0.75
    total_incomes += single_order_price
difference = abs(total_incomes - needed_incomes)
if enough_money:
    print('Target acquired.')
    print(f'Club income - {total_incomes:.2f} leva.')
else:
    print(f'We need {difference:.2f} leva more.')
    print(f'Club income - {total_incomes:.2f} leva.')
