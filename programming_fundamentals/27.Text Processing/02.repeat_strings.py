command_string = input()
command_list = command_string.split()

for element in command_list:
    current_length = len(element)
    print(f'{element * current_length}', end='')
