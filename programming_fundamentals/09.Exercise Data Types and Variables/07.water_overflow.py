times_of_pouring = int(input())
tank_capacity_liters = 255
total_water_in_tank = 0

for _ in range(times_of_pouring):
    current_quantity = int(input())
    if total_water_in_tank + current_quantity <= tank_capacity_liters:
        total_water_in_tank += current_quantity
    else:
        print('Insufficient capacity!')
print(total_water_in_tank)