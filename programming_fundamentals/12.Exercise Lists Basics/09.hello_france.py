items_collection = input().split('|')
budget = float(input())
ticket_to_france_cost = 150
overprice = 1.4
money_is_enough = False
profit = 0
new_prices = []
end_budget = budget

for current_item in items_collection:
    item_separated = current_item.split('->')
    article = item_separated[0]
    price = float(item_separated[1])
    if price > budget:
        continue
    if article == 'Clothes':
        if price > 50:
            continue
    elif article == "Shoes":
        if price > 35:
            continue
    elif article == 'Accessories':
        if price > 20.50:
            continue
    budget -= price
    new_price = price * overprice
    profit += (new_price - price)
    new_prices.append(new_price)
    if budget <= 0:
        break
if end_budget + profit >= ticket_to_france_cost:
    money_is_enough = True
for current_item in range(len(new_prices)):
    if current_item == len(new_prices) - 1:
        print(f'{new_prices[current_item]:.2f}')
    else:
        print(f'{new_prices[current_item]:.2f} ', end='')
print(f'Profit: {profit:.2f}')
if money_is_enough:
    print('Hello, France!')
else:
    print('Not enough money.')
