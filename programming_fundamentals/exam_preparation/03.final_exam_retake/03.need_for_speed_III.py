total_cars = int(input())
need_for_speed_dict = {}

for car in range(total_cars):
    car_command = input()
    car_split = car_command.split('|')
    car_current = car_split[0]
    mileage_current = int(car_split[1])
    fuel_current = int(car_split[2])
    need_for_speed_dict[car_current] = {'mileage': mileage_current, 'fuel': fuel_current}

while True:
    command = input()
    if command == 'Stop':
        break
    command_split = command.split(' : ')
    current_command = command_split[0]
    current_car = command_split[1]
    if current_command == 'Drive':
        current_distance = int(command_split[2])
        current_fuel = int(command_split[3])
        if current_fuel > need_for_speed_dict[current_car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            need_for_speed_dict[current_car]['mileage'] += current_distance
            need_for_speed_dict[current_car]['fuel'] -= current_fuel
            print(f'"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.')
            if need_for_speed_dict[current_car]['mileage'] >= 100000:
                need_for_speed_dict.pop(current_car)
                print(f'Time to sell the {current_car}!')
    elif current_command == 'Refuel':
        current_fuel = int(command_split[2])
        needed_fuel = 75 - need_for_speed_dict[current_car]['fuel']
        if needed_fuel >= current_fuel:
            current_refill = current_fuel
        else:
            current_refill = needed_fuel
        need_for_speed_dict[current_car]['fuel'] += current_refill
        print(f"{current_car} refueled with {current_refill} liters")
    elif current_command == 'Revert':
        current_kilometers = int(command_split[2])
        if need_for_speed_dict[current_car]['mileage'] - current_kilometers < 10000:
            need_for_speed_dict[current_car]['mileage'] = 10000
        else:
            need_for_speed_dict[current_car]['mileage'] -= current_kilometers
            print(f"{current_car} mileage decreased by {current_kilometers} kilometers")
for key_car in need_for_speed_dict:
    print(f"{key_car} -> Mileage: {need_for_speed_dict[key_car]['mileage']} kms, Fuel in the tank: {need_for_speed_dict[key_car]['fuel']} lt.")
