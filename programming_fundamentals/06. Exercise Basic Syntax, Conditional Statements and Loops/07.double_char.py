client_string = input()

while client_string != 'End':
    length = len(client_string)
    doubled_string = ''
    if client_string == 'SoftUni':
        client_string = input()
        continue
    for index in range(length):
        doubled_string += client_string[index] * 2
    print(doubled_string)
    client_string = input()