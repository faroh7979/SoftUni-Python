from collections import deque

water_quantity = int(input())
command_line = input()
people_on_queue = deque()
start_drinking = False

while command_line != 'End':

    if command_line == 'Start':
        start_drinking = True
        command_line = input()

    if start_drinking:
        if ' ' in command_line:
            command = command_line.split()
            refill_liters = int(command[1])
            water_quantity += refill_liters
        else:
            if int(command_line) <= water_quantity:
                water_quantity -= int(command_line)
                drunk_person = people_on_queue.popleft()
                print(f'{drunk_person} got water')
            else:
                drunk_person = people_on_queue.popleft()
                print(f'{drunk_person} must wait')
    else:
        people_on_queue.append(command_line)

    command_line = input()

print(f'{water_quantity} liters left')
