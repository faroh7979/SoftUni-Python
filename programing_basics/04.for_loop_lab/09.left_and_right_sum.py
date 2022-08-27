n = int(input())
left_column_sum = 0
right_column_sum = 0

for i in range(n):
    client_value = int(input())
    left_column_sum += client_value
for i in range(n):
    client_value = int(input())
    right_column_sum += client_value
difference = abs(left_column_sum - right_column_sum)
if left_column_sum == right_column_sum:
    print(f'Yes, sum = {left_column_sum}')
else:
    print(f'No, diff = {difference}')
