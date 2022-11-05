raw_pass = input()
activation_key = raw_pass

while True:
    command = input()
    if command == 'Generate':
        print(f'Your activation key is: {activation_key}')
        break
    command_split = command.split('>>>')
    current_command = command_split[0]
    if current_command == 'Contains':
        current_substring = command_split[1]
        if current_substring in activation_key:
            print(f'{activation_key} contains {current_substring}')
        else:
            print("Substring not found!")
    elif current_command == 'Flip':
        type_of_letters = command_split[1]
        current_start_index = int(command_split[2])
        current_end_index = int(command_split[3])
        if type_of_letters == 'Upper':
            activation_key = activation_key[:current_start_index] +\
                             activation_key[current_start_index: current_end_index].upper() +\
                             activation_key[current_end_index:]
            print(activation_key)
        elif type_of_letters == 'Lower':
            activation_key = activation_key[:current_start_index] +\
                             activation_key[current_start_index: current_end_index].lower() +\
                             activation_key[current_end_index:]
            print(activation_key)
    elif current_command == 'Slice':
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
