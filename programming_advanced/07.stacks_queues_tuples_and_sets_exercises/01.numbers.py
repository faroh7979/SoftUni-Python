first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))

total_commands = int(input())

for _ in range(total_commands):
    current_command = input()
    current_command_split = current_command.split()

    command = current_command_split[0] + " " + current_command_split[1]  # here is the alphabetical command string
    command_length = len(command)
    integer_sequence_starting_index = command_length + 1  # need to include last space after tha alphabetical
    current_command_length = len(current_command)
    # command integer sequence
    integer_sequence_current_input = current_command[integer_sequence_starting_index:current_command_length].split()

    integer_sequence_set = set(map(int, integer_sequence_current_input))  # final sequence for manipulating in set

    if command == 'Add First':
        first_set.update(integer_sequence_set)

    elif command == 'Add Second':
        second_set.update(integer_sequence_set)

    elif command == 'Remove First':
        first_set -= integer_sequence_set

    elif command == 'Remove Second':
        second_set -= integer_sequence_set

    elif command == 'Check Subset':
        check_for_subset = first_set.issubset(second_set) or second_set.issubset(first_set)
        print(check_for_subset)

sorted_first_sequence = sorted(first_set)
sorted_second_sequence = sorted(second_set)
print(', '.join(map(str, sorted_first_sequence)))
print(', '.join(map(str, sorted_second_sequence)))
