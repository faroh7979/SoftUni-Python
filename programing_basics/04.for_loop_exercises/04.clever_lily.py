age_of_lily = int(input())
laundry_price = float(input())
single_toy_price = int(input())
birthday_cash = 0
total_birthday_cash = 0
toy_birthdays = 0
brother_commission = 1

for age in range(1, age_of_lily + 1):
    if age % 2 == 0:
        birthday_cash += 10
        total_birthday_cash += birthday_cash - brother_commission
    else:
        toy_birthdays += 1
total_toys_price = toy_birthdays * single_toy_price
total_lily_cash = total_toys_price + total_birthday_cash
difference = abs(total_lily_cash - laundry_price)

if total_lily_cash >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
