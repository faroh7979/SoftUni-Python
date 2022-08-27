order_nums = int(input())
current_order_price = 0
all_orders_price = 0

for _ in range(order_nums):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if needed_capsule_per_day < 1 or needed_capsule_per_day > 2000:
        continue
    current_order_price = price_per_capsule * days * needed_capsule_per_day
    print(f'The price for the coffee is: ${current_order_price:.2f}')
    all_orders_price += current_order_price
print(f'Total: ${all_orders_price:.2f}')
