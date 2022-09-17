from collections import deque

customer_name = input()
customer_deque = deque()

while customer_name != 'End':

    if customer_name != 'Paid':
        customer_deque.append(customer_name)
    else:
        while customer_deque:
            print(customer_deque.popleft())
    customer_name = input()

left_people = len(customer_deque)
print(f'{left_people} people remaining.')
