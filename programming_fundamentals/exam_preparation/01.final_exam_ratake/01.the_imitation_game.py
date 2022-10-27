crypt_message = input()
final_crypt_message = crypt_message

while True:
    command = input()
    if command == 'Decode':
        break
    command_split = command.split('|')
    command_type = command_split[0]
    if command_type == 'Move':
        letter_count = int(command_split[1])
        final_crypt_message = final_crypt_message[letter_count:] + final_crypt_message[:letter_count]
    elif command_type == 'Insert':
        current_index = int(command_split[1])
        current_value = command_split[2]
        if 0 <= current_index <= len(final_crypt_message):
            final_crypt_message = final_crypt_message[:current_index] + current_value + \
                                  final_crypt_message[current_index:]
    elif command_type == 'ChangeAll':
        current_substring = command_split[1]
        current_replacement = command_split[2]
        final_crypt_message = final_crypt_message.replace(current_substring, current_replacement)
print(f'The decrypted message is: {final_crypt_message}')
