width = int(input())
length = int(input())
height = int(input())
current_used_space = 0
box_volume = 1
apartment_volume = width * length * height

while current_used_space <= apartment_volume:
    current_boxes_num = input()
    if current_boxes_num == 'Done':
        break
    current_boxes_num = int(current_boxes_num)
    current_used_space += current_boxes_num
difference = abs(current_used_space - apartment_volume)
if current_used_space <= apartment_volume:
    print(f'{difference} Cubic meters left.')
else:
    print(f'No more free space! You need {difference} Cubic meters more.')
