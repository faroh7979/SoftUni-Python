total_floors = int(input())
total_rooms = int(input())

for floors in range(total_floors, 0,  - 1):
    for rooms in range(total_rooms):
        if total_floors == 0:
            if rooms == total_rooms - 1:
                print(f'L{floors}{rooms}')
            else:
                print(f'L{floors}{rooms}', end=' ')
        elif floors == total_floors:
            if rooms == total_rooms - 1:
                print(f'L{floors}{rooms}')
            else:
                print(f'L{floors}{rooms}', end=' ')
        elif floors % 2 == 0:
            if rooms == total_rooms - 1:
                print(f'O{floors}{rooms}')
            else:
                print(f'O{floors}{rooms}', end=' ')
        elif floors % 2 != 0:
            if rooms == total_rooms - 1:
                print(f'A{floors}{rooms}')
            else:
                print(f'A{floors}{rooms}', end=' ')
