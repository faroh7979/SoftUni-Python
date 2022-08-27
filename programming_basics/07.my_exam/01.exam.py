from math import ceil
average_speed = float(input())
liters_per_100_km = float(input())
total_distance = 384400
staying_period = 3

total_hours = total_distance * 2 / average_speed + staying_period
total_fuel = (total_distance * 2) / 100 * liters_per_100_km

print(f'{ceil(total_hours):.0f}')
print(f'{total_fuel:.0f}')

