total_park_operations = int(input())
unique_numbers = set()

for _ in range(total_park_operations):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        unique_numbers.add(car_number)

    elif direction == 'OUT':
        unique_numbers.remove(car_number)

if unique_numbers:
    for number in unique_numbers:
        print(number)

else:
    print('Parking Lot is Empty')
