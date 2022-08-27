n = int(input())
total = 0
max_number = float('-inf')

for i in range(n):
    client_value = int(input())
    if client_value > max_number:
        max_number = client_value
    total += client_value
net_total = total - max_number
difference = abs(net_total - max_number)

if net_total == max_number:
    print('Yes')
    print(f'Sum = {net_total}')
else:
    print('No')
    print(f'Diff = {difference}')
