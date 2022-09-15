registration_numbers = int(input())
reg_dic = {}

for _ in range(registration_numbers):
    command_line = input().split()
    command = command_line[0]
    if command == 'register':
        username = command_line[1]
        registration_plate = command_line[2]
        if username in reg_dic:
            print(f"ERROR: already registered with plate number {reg_dic[username]}")
        else:
            reg_dic[username] = registration_plate
            print(f"{username} registered {registration_plate} successfully")
    elif command == 'unregister':
        username = command_line[1]
        if username not in reg_dic:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            reg_dic.pop(username)
for key in reg_dic:
    print(f"{key} => {reg_dic[key]}")
