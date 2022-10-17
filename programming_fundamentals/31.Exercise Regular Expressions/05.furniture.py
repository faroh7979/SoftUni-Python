import re

furniture_pattern = r'(?<=\>{2})([A-Za-z]+)\<\<(\d+\.?\d*)\!(\d+)'
furniture_list = []
total_final_price = 0

while True:
    command_furniture = input()
    if command_furniture == 'Purchase':
        break
    order = re.findall(furniture_pattern, command_furniture)
    if order:
        current_furniture = order[0][0]
        current_price = float(order[0][1])
        current_quantity = int(order[0][2])
        furniture_list.append(current_furniture)
        current_total_price = current_price * current_quantity
        total_final_price += current_total_price
print('Bought furniture:')
if total_final_price > 0:
    print('\n'.join(furniture_list))
print(f'Total money spend: {total_final_price:.2f}', end='')
