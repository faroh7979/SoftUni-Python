old_pass = input()
reset_pass = old_pass

while True:
    command_line = input()
    if command_line == 'Done':
        break
    elif command_line == 'TakeOdd':
        reset_pass = reset_pass[1::2]
        print(reset_pass)
        continue
    command_split = command_line.split()
    command = command_split[0]
    if command == 'Cut':
        current_index = int(command_split[1])
        current_length = int(command_split[2])
        reset_pass = reset_pass[:current_index] + reset_pass[current_index + current_length:]
        print(reset_pass)
    elif command == 'Substitute':
        current_substring = command_split[1]
        current_substitute = command_split[2]
        if current_substring in reset_pass:
            reset_pass = reset_pass.replace(current_substring, current_substitute)
            print(reset_pass)
        else:
            print('Nothing to replace!')
print(f'Your password is: {reset_pass}')
