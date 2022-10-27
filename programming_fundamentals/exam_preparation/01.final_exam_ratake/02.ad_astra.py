import re

solar_string = input()
daily_portion = 2000
items_list = []
total_calories = 0
solar_pattern = r'#([A-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([A-z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
item_products = re.findall(solar_pattern, solar_string)
for current_index in range(0, len(item_products)):
    if item_products[current_index][0]:
        items_list.append(f'Item: {item_products[current_index][0]}, Best before: {item_products[current_index][1]}, Nutrition: {item_products[current_index][2]}')
        total_calories += int(item_products[current_index][2])
    else:
        items_list.append(f'Item: {item_products[current_index][3]}, Best before: {item_products[current_index][4]}, Nutrition: {item_products[current_index][5]}')
        total_calories += int(item_products[current_index][5])
days_with_food = total_calories // daily_portion
print(f'You have food to last you for: {days_with_food} days!')
if items_list:
    print(f'\n'.join(items_list), sep='')
