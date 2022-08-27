width = int(input())
length = int(input())
cake_area = width * length
cake_is_enough = False

while cake_area > 0:
    pieces = input()
    if pieces == 'STOP':
        cake_is_enough = True
        break
    pieces = int(pieces)
    cake_area -= pieces
if cake_is_enough:
    print(f'{cake_area} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_area)} pieces more.')
