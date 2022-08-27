long_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())

aquarium_area = long_cm * 0.1 * width_cm * 0.1 * height_cm * 0.1

needed_water_liters = aquarium_area - aquarium_area * percentage / 100

print(needed_water_liters)
