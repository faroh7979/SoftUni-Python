import sys

total_bottles_preparation = int(input())
quantity_per_bottle = 750
plate_preparation = 5
pot_preparation = 15
preparation_expense = 0
total_clean_plates = 0
total_clean_pots = 0
for washes in range(1, sys.maxsize):
    current_dishes = input()
    if current_dishes == 'End':
        break
    if washes % 3 == 0:
        preparation_expense += int(current_dishes) * pot_preparation
        total_clean_pots += int(current_dishes)
    else:
        preparation_expense += int(current_dishes) * plate_preparation
        total_clean_plates += int(current_dishes)
    if preparation_expense > total_bottles_preparation * quantity_per_bottle:
        break

difference = abs(preparation_expense - total_bottles_preparation * quantity_per_bottle)
if preparation_expense <= total_bottles_preparation * quantity_per_bottle:
    print('Detergent was enough!')
    print(f'{total_clean_plates} dishes and {total_clean_pots} pots were washed.')
    print(f'Leftover detergent {difference} ml.')
else:
    print(f'Not enough detergent, {difference} ml. more necessary!')
