sequence_target = input()
sequence_target_list = list(map(int, sequence_target.split()))

while True:
    command_str = input()
    if command_str == 'End':
        break
    command = command_str.split()
    if command[0] == 'Shoot':
        current_index = int(command[1])
        current_power = int(command[2])
        if current_index < 0 or current_index >= len(sequence_target_list):
            continue
        sequence_target_list[current_index] -= current_power
        if sequence_target_list[current_index] <= 0:
            sequence_target_list.pop(current_index)
    elif command[0] == 'Add':
        current_index = int(command[1])
        current_value = int(command[2])
        if current_index < 0 or current_index >= len(sequence_target_list):
            print("Invalid placement!")
            continue
        sequence_target_list.insert(current_index, current_value)
    elif command[0] == 'Strike':
        current_index = int(command[1])
        current_radius = int(command[2])
        radius_before = current_index - current_radius
        radius_after = current_index + current_radius
        if current_index < 0 or current_index >= len(sequence_target_list) or\
                radius_before < 0 or radius_before >= len(sequence_target_list) or\
                radius_after < 0 or radius_after >= len(sequence_target_list):
            print("Strike missed!")
            continue
        for removed_index in range(radius_before, radius_after + 1):
            sequence_target_list.pop(current_index - current_radius)
print(* sequence_target_list, sep='|')
