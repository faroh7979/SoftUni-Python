voucher_value = int(input())
item = input()
item_symbols = 0
item_price = 0
total_tickets = 0
other_items = 0
total_spend = 0
while item != 'End':
    item_symbols = len(item)
    if item_symbols > 8:
        total_tickets += 1
        item_price = ord(item[0]) + ord(item[1])
    else:
        other_items += 1
        item_price = ord(item[0])
    total_spend += item_price
    if total_spend > voucher_value:
        if item_symbols > 8:
            total_tickets -= 1
        else:
            other_items -= 1
        break
    item = input()
print(total_tickets)
print(other_items)
