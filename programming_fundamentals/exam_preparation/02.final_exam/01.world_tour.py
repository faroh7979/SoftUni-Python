destinations = input()
new_string_destination = destinations
while True:
    command = input()
    if command == 'Travel':
        break
    command_split = command.split(':')
    if command_split[0] == 'Add Stop':
        current_index = int(command_split[1])
        current_string = command_split[2]
        if 0 <= current_index < len(new_string_destination):
            new_string_destination = new_string_destination[:current_index] +\
                         current_string + new_string_destination[current_index:]
        print(new_string_destination)
    elif command_split[0] == 'Remove Stop':
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        if 0 <= start_index < len(new_string_destination) and 0 <= end_index < len(new_string_destination):
            new_string_destination = new_string_destination[:start_index] + new_string_destination[end_index + 1:]
        print(new_string_destination)
    elif command_split[0] == 'Switch':
        old_string = command_split[1]
        new_string = command_split[2]
        if old_string in new_string_destination:
            new_string_destination = new_string_destination.replace(old_string, new_string)
        print(new_string_destination)
print(f"Ready for world tour! Planned stops: {new_string_destination}")
