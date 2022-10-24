command_string = input()
final_string = command_string

while True:
    command_line = input()

    if command_line == 'End':
        break

    command_split = command_line.split()
    command = command_split[0]

    if command == 'Translate':
        translate_char = command_split[1]
        translate_replacement = command_split[2]

        final_string = final_string.replace(translate_char, translate_replacement)
        print(final_string)

    elif command == 'Includes':
        current_substring = command_split[1]
        includes = False

        if current_substring in final_string:
            includes = True
        print(includes)

    elif command == 'Start':
        start_substring = command_split[1]
        starts_with = False

        if final_string.startswith(start_substring):
            starts_with = True
        print(starts_with)

    elif command == 'Lowercase':
        final_string = final_string.lower()
        print(final_string)

    elif command == 'FindIndex':
        find_char = command_split[1]
        final_index = len(final_string) - final_string[::-1].find(find_char) - 1
        print(final_index)

    elif command == 'Remove':
        start_index = int(command_split[1])
        count = int(command_split[2])
        final_string = final_string[:start_index] + final_string[start_index + count:]
        print(final_string)
