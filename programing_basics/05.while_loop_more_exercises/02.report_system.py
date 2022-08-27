from sys import maxsize

needed_money = int(input())
card_raised_money = 0
cash_raised_money = 0
total_successful_transactions_cash = 0
total_successful_transactions_card = 0

for transaction_num in range(1, maxsize):
    amount = input()
    if amount == 'End':
        break
    if transaction_num % 2 != 0:
        if int(amount) <= 100:
            cash_raised_money += int(amount)
            total_successful_transactions_cash += 1
            print("Product sold!")
        else:
            print('Error in transaction!')
    else:
        if int(amount) >= 10:
            card_raised_money += int(amount)
            total_successful_transactions_card += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    if card_raised_money + cash_raised_money >= needed_money:
        break
if total_successful_transactions_cash > 0:
    average_cash = cash_raised_money / total_successful_transactions_cash
    average_card = card_raised_money / total_successful_transactions_card
    if card_raised_money + cash_raised_money >= needed_money:
        print(f'Average CS: {average_cash:.2f}')
        print(f'Average CC: {average_card:.2f}')
    else:
        print('Failed to collect required money for charity.')
else:
    if card_raised_money + cash_raised_money >= needed_money:
        average_card = cash_raised_money / total_successful_transactions_card
        print(f'Average CS: {average_card:.2f}')
    else:
        print('Failed to collect required money for charity.')
