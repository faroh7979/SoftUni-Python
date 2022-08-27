from math import floor
total_balls = int(input())
total_points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
other_count = 0

for balls in range(total_balls):
    colour_ball = input()
    if colour_ball == 'red':
        total_points += 5
        red_count += 1
    elif colour_ball == 'orange':
        total_points += 10
        orange_count += 1
    elif colour_ball == 'yellow':
        total_points += 15
        yellow_count += 1
    elif colour_ball == 'white':
        total_points += 20
        white_count += 1
    elif colour_ball == 'black':
        total_points //= 2
        black_count += 1
    else:
        other_count += 1

print(f'Total points: {total_points}')
print(f'Red balls: {red_count}')
print(f'Orange balls: {orange_count}')
print(f'Yellow balls: {yellow_count}')
print(f'White balls: {white_count}')
print(f'Other colors picked: {other_count}')
print(f'Divides from black balls: {black_count}')
