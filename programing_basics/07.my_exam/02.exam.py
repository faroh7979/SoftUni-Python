from math import floor
width = float(input())
length = float(input())
height = float(input())
average_human_height = float(input())

total_volume = width * length * height
single_cabin_volume = 2 * 2 * (average_human_height + 0.40)

total_human = floor(total_volume / single_cabin_volume)

if 3 <= total_human <= 10:
    print(f'The spacecraft holds {total_human} astronauts.')
elif total_human < 3:
    print( "The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
    