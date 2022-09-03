total_wagons = int(input())
command = input()
train = []
train += '0' * total_wagons
train = list(map(int, train))

while command != 'End':
    list_command = command.split(' ')
    command_type = list_command[0]
    if command_type == 'add':
        people = int(list_command[1])
        train[total_wagons - 1] += people
    elif command_type == 'insert':
        people = int(list_command[2])
        current_wagon = int(list_command[1])
        train[current_wagon] += people
    elif command_type == 'leave':
        people = int(list_command[2])
        current_wagon = int(list_command[1])
        train[current_wagon] -= people
    command = input()
print(train)
