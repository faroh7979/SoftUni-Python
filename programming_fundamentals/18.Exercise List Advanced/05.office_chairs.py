total_rooms = int(input())
total_free_chairs = 0
enough_chairs = True
for current_room in range(1, total_rooms + 1):
    chairs_guests = input().split()
    current_chairs = len(chairs_guests[0])
    current_guests = int(chairs_guests[1])
    if current_chairs >= current_guests:
        total_free_chairs += current_chairs - current_guests
    else:
        print(f'{current_guests - current_chairs} more chairs needed in room {current_room}')
        enough_chairs = False
if enough_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
