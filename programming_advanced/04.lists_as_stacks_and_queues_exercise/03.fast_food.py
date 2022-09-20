from collections import deque

total_prepared_food = int(input())
all_orders = input().split()
orders_queue = deque(map(int, all_orders))
enough_food = True
orders_left = ''

print(max(orders_queue))

for _ in range(len(orders_queue)):
    current_quantity = orders_queue.popleft()
    if current_quantity <= total_prepared_food:
        total_prepared_food -= current_quantity
    else:
        orders_left = f"{current_quantity} {' '.join(map(str, orders_queue))}"
        enough_food = False
        break

if enough_food:
    print('Orders complete')
else:
    print(f'Orders left: {orders_left}')
