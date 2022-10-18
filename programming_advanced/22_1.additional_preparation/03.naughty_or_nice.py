def naughty_or_nice_list(full_kids: list, *commands, **kwargs_commands):
    nice = []
    naughty = []
    final_string = ''

    for command in commands:
        searched_num, list_to_move = command.split('-')
        total_matches = 0
        name = ''
        value_to_first_remove = ''

        for value in full_kids:
            if value[0] == int(searched_num):
                total_matches += 1
                name = value[1]
                value_to_first_remove = value
                if total_matches == 2:
                    break

        if total_matches == 1:
            if list_to_move == 'Nice':
                nice.append(name)
            else:
                naughty.append(name)
            full_kids.remove(value_to_first_remove)

    if kwargs_commands:
        for current_name, new_list in kwargs_commands.items():
            match = False
            current_matches = 0
            value_to_remove = ''
            for element in full_kids:
                if current_name == element[1]:
                    current_matches += 1
                    value_to_remove = element
                    match = True
                    if current_matches == 2:
                        match = False
                        break
            if match:
                if new_list == "Naughty":
                    naughty.append(current_name)
                else:
                    nice.append(current_name)
                full_kids.remove(value_to_remove)

    not_found = [i[1] for i in full_kids]

    if nice:
        final_string += f'Nice: {", ".join(nice)}\n'

    if naughty:
        final_string += f'Naughty: {", ".join(naughty)}\n'

    if not_found:
        final_string += f'Not found: {", ".join(not_found)}\n'

    return final_string


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
