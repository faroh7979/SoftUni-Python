conceals_message = input()
final_message = conceals_message

while True:
    command = input()
    if command == 'Reveal':
        print(f"You have a new text message: {final_message}")
        break
    command_split = command.split(':|:')
    current_command = command_split[0]
    if current_command == 'InsertSpace':
        current_index = int(command_split[1])
        final_message = final_message[:current_index] + ' ' + final_message[current_index:]
        print(final_message)
    elif current_command == 'Reverse':
        current_substring = command_split[1]
        if current_substring not in final_message:
            print('error')
        else:
            substring_starting_index = final_message.index(current_substring)
            final_message = final_message[:substring_starting_index] +\
                final_message[substring_starting_index + len(current_substring):] +\
                current_substring[::-1]
            print(final_message)
    elif current_command == 'ChangeAll':
        change_substring = command_split[1]
        replacement = command_split[2]
        final_message = final_message.replace(change_substring, replacement)
        print(final_message)
