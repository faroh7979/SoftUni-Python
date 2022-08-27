needed_money = float(input())
budget = float(input())
spend_times_in_row = 0
has_needed_money = True
days_left = 0

while budget < needed_money:
    if spend_times_in_row == 5:
        has_needed_money = False
        break
    operation_type = input()
    amount = float(input())
    if operation_type == 'spend':
        if amount > budget:
            amount = budget
        amount = -amount
        spend_times_in_row += 1
    elif operation_type == 'save':
        amount = amount
        spend_times_in_row = 0
    days_left += 1
    budget += amount
if has_needed_money:
    print(f'You saved the money for {days_left} days.')
else:
    print("You can't save the money.")
    print(days_left)
