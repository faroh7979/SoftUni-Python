client_order = input().split('|')
command_numbers = client_order.count('-')
client_order_length = client_order.__len__()
energy = 100
coins = 100
manage_to_handle = True

for current_order in range(client_order_length):
    separator_index = client_order[current_order].index("-")
    order_type = client_order[current_order][:separator_index:]
    order_value = int(client_order[current_order][separator_index + 1::])
    if order_type == 'rest':
        if energy + order_value <= 100:
            energy += order_value
            gained_energy = order_value
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f'You gained {gained_energy} energy.')
        print(f"Current energy: {energy}.")
    elif order_type == 'order':
        if energy >= 30:
            coins += order_value
            energy -= 30
            print(f"You earned {order_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
            if energy > 100:
                energy = 100
    else:
        if order_value <= coins:
            print(f"You bought {order_type}.")
            coins -= order_value
        else:
            manage_to_handle = False
            print(f"Closed! Cannot afford {order_type}.")
            break
if manage_to_handle:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
