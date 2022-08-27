daily_pocket_money = float(input())
daily_incomes = float(input())
total_expense = float(input())
present_price = float(input())
days_remaining = 5

total_incomes = daily_incomes * days_remaining + daily_pocket_money * days_remaining
budget = total_incomes - total_expense
difference = abs(budget - present_price)

if budget >= present_price:
    print(f'Profit: {budget:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {difference:.2f} BGN.')
