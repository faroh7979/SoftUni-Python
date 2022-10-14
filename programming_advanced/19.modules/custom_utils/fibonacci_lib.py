def create_sequence(up_to_number=1000):
    fibonacci_start = [0, 1]

    for _ in range(up_to_number - 2):  # because we are starting with default values in list above
        current_num_to_append = fibonacci_start[-1] + fibonacci_start[-2]
        fibonacci_start.append(current_num_to_append)

    return fibonacci_start


def fibonacci_command():
    while True:
        current_command = input()

        if current_command == 'Stop':
            return ''

        command = current_command.split()

        if command[0] == 'Create':
            total_nums = int(command[2])

            sequence = create_sequence(total_nums)

            print(" ".join(map(str, sequence)))

        elif command[0] == 'Locate':
            searched_num = int(command[1])

            sequence = create_sequence()

            if searched_num in sequence:
                print(f'The number - {searched_num} is at index {sequence.index(searched_num)}')

            else:
                print(f'The number {searched_num} is not in the sequence')

