order_dict = {}

while True:
    command_line = input()
    if command_line == 'buy':
        break
    product, price, quantity = command_line.split()
    if product not in order_dict:
        order_dict[product] = [float(price), float(quantity)]
    else:
        order_dict[product][0] = float(price)
        order_dict[product][1] += float(quantity)
for key in order_dict:
    print(f'{key} -> {order_dict[key][0] * order_dict[key][1]:.2f}')
