current_dict = {}
position = 1

while True:
    command = input()
    if command == 'stop':
        break
    if position % 2 != 0:
        current_key = command
        if current_key not in current_dict:
            current_dict[current_key] = 0
    else:
        current_value = int(command)
        current_dict[current_key] += current_value
    position += 1
for key, value in current_dict.items():
    print(f'{key} -> {value}')
