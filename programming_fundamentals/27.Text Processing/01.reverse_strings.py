while True:
    command = input()
    if command == 'end':
        break
    reversed_string = command[::-1]
    print(f'{command} = {reversed_string}')
