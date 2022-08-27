from math import floor
from math import ceil

x_area_meters = int(input())
y_grape_per_meter = float(input())
z_needed_liters = int(input())
total_workers = int(input())

total_meters_for_wine = x_area_meters * 0.4
total_grape = y_grape_per_meter * total_meters_for_wine
total_wine_liters = total_grape / 2.5

difference = abs(total_wine_liters - z_needed_liters)
wine_for_workers_liters = difference / total_workers

if total_wine_liters < z_needed_liters:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_wine_liters)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_for_workers_liters)} liters per person.")
