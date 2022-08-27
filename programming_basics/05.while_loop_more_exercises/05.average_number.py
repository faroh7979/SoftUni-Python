numbers = int(input())
total = 0

for i in range(numbers):
    current_number = int(input())
    total += current_number
average = total / numbers
print(f'{average:.2f}')
