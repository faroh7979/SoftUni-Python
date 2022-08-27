from math import ceil
height = int(input())
width = int(input())
needless_percentage = int(input())
total_area_needed_to_be_painted = ceil((height * width * 4) * ((100 - needless_percentage) / 100))
total_painted = 0
paint_command = input()

while paint_command != 'Tired!':
    paint_command = int(paint_command)
    total_painted += paint_command
    if total_area_needed_to_be_painted <= total_painted:
        break
    paint_command = input()
difference = abs(total_area_needed_to_be_painted - total_painted)

if total_area_needed_to_be_painted > total_painted:
    print(f'{difference} quadratic m left.')
elif difference == 0:
    print('All walls are painted! Great job, Pesho!')
elif total_painted > total_area_needed_to_be_painted:
    print(f'All walls are painted and you have {difference} l paint left!')
