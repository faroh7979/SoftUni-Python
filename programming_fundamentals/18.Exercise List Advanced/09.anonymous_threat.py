worm = input()
worm_list = worm.split()
help_list = []
help_string = ''
help_join = ''

while True:
    command_begin = input()
    if command_begin == '3:1':
        break
    command = command_begin.split()
    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(worm_list):
            end_index = len(worm_list) - 1
        help_join = ''.join(worm_list[start_index:end_index + 1])
        worm_list[start_index:end_index + 1] = [help_join]
    elif command[0] == 'divide':
        current_index = int(command[1])
        partitions = int(command[2])
        whole_part = len(worm_list[current_index]) // partitions
        rest_part = len(worm_list[current_index]) % partitions
        for main_loop in range(0, partitions):
            help_string = ''
            for second_loop in range(main_loop * whole_part, main_loop * whole_part + whole_part):
                help_string += worm_list[current_index][second_loop]
            if main_loop == partitions - 1:
                for rest in range(main_loop * whole_part + whole_part, len(worm_list[current_index])):
                    help_string += worm_list[current_index][rest]
            help_list.append(help_string)
        worm_list.insert(current_index, ' '.join(help_list))
        worm_list.pop(current_index + 1)
print(' '.join(worm_list))
