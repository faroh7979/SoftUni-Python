def left_move():
    return 0, -1


def right_move():
    return 0, 1


def up_move():
    return -1, 0


def down_move():
    return 1, 0


rows, cols = 6, 6

matrix = [[i for i in input().split()]for _ in range(rows)]
starting_position = input().split(', ')

starting_row = int(starting_position[0][1])
starting_col = int(starting_position[1][-2])

command_input = input()
while command_input != 'Stop':
    command_split = command_input.split(', ')
    command = command_split[0]
    direction = command_split[1]

    if command == 'Create':
        value = command_split[2]

        if direction == 'up':
            direction_row, direction_col = up_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'down':
            direction_row, direction_col = down_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'left':
            direction_row, direction_col = left_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'right':
            direction_row, direction_col = right_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        if matrix[starting_row][starting_col] == '.':
            matrix[starting_row][starting_col] = value

    elif command == 'Update':
        value = command_split[2]

        if direction == 'up':
            direction_row, direction_col = up_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'down':
            direction_row, direction_col = down_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'left':
            direction_row, direction_col = left_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'right':
            direction_row, direction_col = right_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        if matrix[starting_row][starting_col] != '.':
            matrix[starting_row][starting_col] = value

    elif command == 'Read':

        if direction == 'up':
            direction_row, direction_col = up_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'down':
            direction_row, direction_col = down_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'left':
            direction_row, direction_col = left_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'right':
            direction_row, direction_col = right_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        if matrix[starting_row][starting_col] != '.':
            print(matrix[starting_row][starting_col])

    elif command == 'Delete':

        if direction == 'up':
            direction_row, direction_col = up_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'down':
            direction_row, direction_col = down_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'left':
            direction_row, direction_col = left_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        elif direction == 'right':
            direction_row, direction_col = right_move()
            possible_starting_row = starting_row + direction_row
            possible_starting_col = starting_col + direction_col

            if possible_starting_row < 0 or possible_starting_row >= rows \
                    or possible_starting_col < 0 or possible_starting_col >= cols:
                continue

            starting_row = possible_starting_row
            starting_col = possible_starting_col

        if matrix[starting_row][starting_col] != '.':
            matrix[starting_row][starting_col] = '.'

    command_input = input()

for row in matrix:
    print(" ".join(row))
