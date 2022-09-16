def user_in_side(checked_string, my_def_dict):
    for every_key in my_def_dict:
        for current_def_index in range(0, len(my_def_dict[every_key])):
            if my_def_dict[every_key][current_def_index] == checked_string:
                return True
    return False


traitor_found = False
force_dict = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if " | " in command:
        force_side, force_user = command.split(' | ')
        if not user_in_side(force_user, force_dict):
            if force_side not in force_dict:
                force_dict[force_side] = [force_user]
            else:
                force_dict[force_side].append(force_user)
    elif " -> " in command:
        force_user, force_side = command.split(' -> ')
        if not user_in_side(force_user, force_dict):
            if force_side not in force_dict:
                force_dict[force_side] = [force_user]
            else:
                force_dict[force_side].append(force_user)
        else:
            for current_side in force_dict:
                if traitor_found:
                    traitor_found = False
                    break
                for current_value in force_dict[current_side]:
                    if force_dict == current_value:
                        force_dict[current_side].remove(current_value)
                        force_dict[force_side].append(force_user)
                        traitor_found = True
                        break
for current_key in force_dict:
    current_key_len = len(force_dict[current_key])
    if current_key_len > 0:
        print(f'Side: {current_key}, Members: {current_key_len}')
        for elements in force_dict[current_key]:
            print(f'! {elements}')
