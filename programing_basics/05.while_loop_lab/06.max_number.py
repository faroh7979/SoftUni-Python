from sys import maxsize
customer_input = input()
max_value = -maxsize

while customer_input != 'Stop':
    current_value = int(customer_input)
    if max_value <= current_value:
        max_value = current_value
    customer_input = input()
print(max_value)
