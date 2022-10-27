total_capacity = int(input())
users_dict = {}

while True:
    command_line = input()
    if command_line == 'Statistics':
        break

    command_split = command_line.split('=')
    command = command_split[0]

    if command == 'Add':
        adding_username = command_split[1]
        adding_sent = int(command_split[2])
        adding_received = int(command_split[3])

        if adding_username not in users_dict:
            users_dict[adding_username] = {'sent': adding_sent, 'received': adding_received}

    elif command == 'Message':
        sender = command_split[1]
        receiver = command_split[2]

        if sender in users_dict and receiver in users_dict:
            users_dict[sender]['sent'] += 1
            users_dict[receiver]['received'] += 1

            if users_dict[sender]['sent'] + users_dict[sender]['received'] >= total_capacity:
                users_dict.pop(sender)
                print(f"{sender} reached the capacity!")

            if users_dict[receiver]['sent'] + users_dict[receiver]['received'] >= total_capacity:
                users_dict.pop(receiver)
                print(f"{receiver} reached the capacity!")

    elif command == 'Empty':
        empty_username = command_split[1]

        if empty_username == 'All':
            users_dict = {}
        else:
            users_dict.pop(empty_username)

total_users = len(users_dict)
print(f'Users count: {total_users}')

for key in users_dict:
    total_message = users_dict[key]['sent'] + users_dict[key]['received']
    print(f'{key} - {total_message}')
