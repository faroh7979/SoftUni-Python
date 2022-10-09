from os import path, remove


def create_file(file_name):
    file_path = f'./{file_name}'

    with open(file_path, 'w') as file_to_add:
        file_to_add.write('')


def add_file(file_name, content):
    file_path = f'./{file_name}'

    if path.exists(file_path):  # if file exists
        with open(file_path, 'a') as appending_file:
            appending_file.write(f'{content}\n')

    else:
        with open(file_path, 'w') as adding_file:
            adding_file.write(f'{content}\n')


def replace_in_file(file_name, old_string, new_string):
    file_path = f'./{file_name}'

    if path.exists(file_path):
        with open(file_path, 'r') as file_to_replace:
            old_content = file_to_replace.read()
            new_content = old_content.replace(old_string, new_string)  # using to overwrite the old file

        with open(file_path, 'w') as file_replacing:
            file_replacing.write(new_content)

    else:
        print('An error occurred')


def delete_file(file_name):
    file_path = f'./{file_name}'

    if path.exists(file_path):
        remove(file_path)

    else:
        print('An error occurred')


command = input()
while command != 'End':
    command_split = command.split('-')

    command_type = command_split[0]
    file_name = command_split[1]

    if command_type == 'Create':
        create_file(file_name)

    elif command_type == 'Add':
        content = command_split[2]

        add_file(file_name, content)

    elif command_type == 'Replace':
        old_string = command_split[2]
        new_string = command_split[3]

        replace_in_file(file_name, old_string, new_string)

    elif command_type == 'Delete':
        delete_file(file_name)

    command = input()
